import six
import time
from ..common import PyEXception


_DATA_TYPES = [
    'boolean',
    'date',
    'dynamictime',
    'event',
    'number',
    'number',
    'string'
]


def _tryEx(meth, name, userDat=None):
    try:
        meth()
    except TypeError:
        if userDat is not None:
            raise PyEXception('Construction of {} errored, malformed user data: {}'.format(name, userDat))
        raise PyEXception('Construction of {} errored: malformed data!'.format(name))


class Input(object):
    def __init__(self, engine, label, value, type, scope, isLookup=False, weight=0, weightKey=''):
        self.engine = engine
        self.label = label
        self.value = value
        self.type = type
        self.scope = scope
        self.isLookup = isLookup
        self.weight = weight
        self.weightKey = weightKey

    def toJson(self):
        return {
            'label': self.label,
            'value': self.value,
            'type': self.type,
            'scope': self.scope,
            'isLookup': self.isLookup,
            'weight': self.weight,
            'weightKey': self.weightKey
        }


class Operator(object):
    def __init__(self, type, label, value):
        self.type = type
        self.label = label
        self.value = value

    def toJson(self):
        return {
            'type': self.type,
            'label': self.label,
            'value': self.value
        }


class NotificationType(object):
    def __init__(self, engine, label, value, weight, enabled, schema=None):
        self.engine = engine
        self.label = label
        self.value = value
        self.weight = weight
        self.enabled = enabled
        self.schema = schema or {}

    def toJson(self):
        return {
            'label': self.label,
            'value': self.value,
            'weight': self.weight,
            'enabled': self.enabled,
            'schema': self.schema,
        }

    def validate(self, output):
        if self.schema:
            try:
                from jsonschema import validate
                validate(instance=output.toJson(), schema=self.schema)
            except ImportError:
                raise PyEXception('jsonschema package required for schema validation')


class Output(object):
    def __init__(self, engine, notificationType, **kwargs):
        self.engine = engine
        self.notificationType = notificationType
        self.notificationType.validate(self)
        self.kwargs = kwargs

    def toJson(self):
        return self.kwargs

    def validate(self):
        self.notificationType.validate(self)


class Condition(object):
    def __init__(self, engine, left_value, operator, right_value):
        self.engine = engine
        self.left_value = self._constructValue(left_value)
        self.operator = self._constructOperator(operator)
        self.right_value = self._constructDependentValue(right_value)
        self._validate()

    def _constructValue(self, val):
        if isinstance(val, Input):
            # already fine
            return val
        return self.engine.input(val)

    def _constructOperator(self, val):
        '''this operator is dependent on the type of the left value.

        Note that this will only do partial validation, to avoid extra API calls
        '''
        if isinstance(val, Operator):
            # already fine
            ret = val
        else:
            ret = self.engine.operator(val)

        if self.left_value.type != ret.type:
            raise PyEXception('Input {} does not match operator {}'.format(self.left_value.toJson(), ret.toJson()))
        return ret

    def _constructDependentValue(self, val):
        '''this value is dependent on the type of the operator

        Note that this will only do partial validation, to avoid extra API calls
        '''
        if self.operator.type == 'number':
            if not isinstance(val, (int, float)):
                raise PyEXception('RValue of type (int, float) expected for operator {}, got {}'.format(self.operator.toJson(), val))
        elif self.operator.type == 'string':
            if not isinstance(val, six.string_types):
                raise PyEXception('RValue of type str expected for operator {}, got {}'.format(self.operator.toJson(), val))
        elif self.operator.type == 'boolean':
            if not isinstance(val, bool):
                raise PyEXception('RValue of type bool expected for operator {}, got {}'.format(self.operator.toJson(), val))
        elif self.operator.type == 'time':
            # format in HH:MM:SS - HH:MM:SS
            try:
                left, right = val.split('-')
                time.strptime(left.strip(), '%H:%M:%S')
                time.strptime(right.strip(), '%H:%M:%S')
            except (IndexError, ValueError):
                raise PyEXception('Malformed time: {}'.format(val))
        return val

    def validate(self):
        '''In this instance, we just need to check that the rvalue
        matches the options for the lvalue when lvalue.isLookup is true'''
        # TODO

    def toJson(self):
        return [self._left_value.value,
                self._operator.value,
                self._right_value]


class Rule(object):
    def __init__(self, engine, conditions, outputs, additionalKeys=None):
        self._engine = engine
        additionalKeys = additionalKeys or []

        # do some rudimentary initial validation
        if not isinstance(conditions, list):
            raise PyEXception('conditions must be list of list[str] or Condition')
        self._conditions = conditions

        if not isinstance(outputs, list) or len(outputs) != 1 or not isinstance(outputs[0], (Output, dict)):
            raise PyEXception('outputs must be List[dict] or List[Output] of length 1')
        self._outputs = outputs

        if not isinstance(additionalKeys, list):
            raise PyEXception('additionalKeys must be List[str] or List[Input]')
        self._additionalKeys = additionalKeys

        self._construct()

    def _construct(self):
        _tryEx(self._constructConditions, 'conditions', self._conditions)
        _tryEx(self._constructOutputs, 'outputs', self._outputs)
        _tryEx(self._constructAdditionalKeys, 'additionalKeys', self._additionalKeys)

    def _constructHelper(self, type, lst):
        # Convert x to type
        for i, t in enumerate(lst):
            if isinstance(t, type):
                continue
            lst[i] = type(self._engine, *t)

    def _constructConditions(self):
        # Convert conditions to Condition
        self._constructHelper(Condition, self._conditions)

    def _constructOutputs(self):
        # Convert outputs to Output
        self._constructHelper(Output, self._outputs)

    def _constructAdditionalKeys(self):
        # Convert keys to Input
        self._constructHelper(Input, self._additionalKeys)

    def toJson(self):
        return {
            'conditions': [c.toJson() for c in self._conditions],
            'outputs': [o.toJson() for o in self._outputs],
            'additionalKeys': [a.value for a in self._additionalKeys]
        }

    def validate(self, prompt=True):
        '''
        Validate that this rule is correctly formed. Some rules can be asserted at time of
        object construction, however some schema validation might require additional API calls,
        which is why this method is separated.
        '''
        if prompt:
            if input('Validating rule, this function may incur additional API usage...type q to quit') == 'q':
                return
        for x in self._conditions + self._outputs + self._additionalKeys:
            x.validate()


class RulesEngine(object):
    def __init__(self, schema, version, token):
        self.reinitialize(schema, version, token)

    def reinitialize(self, schema, version, token):
        self._schema = schema
        self._version = version
        self._token = token
        self._construct()

    def _construct(self):
        _tryEx(self._constructOperators, 'operators')
        _tryEx(self._constructNotifications, 'notificationTypes')
        _tryEx(self._constructInputs, 'schema')

    def _constructOperators(self):
        self._operators = {}
        for k, v in self._schema['operators'].items():
            self._operators[k] = [Operator(self, k, **vv) for vv in v]

    def operator(self, key):
        for k in self.operators():
            if k == key:
                return self._operators[key]
        raise PyEXception('Operator not found: {}'.format(key))

    def operators(self):
        for k in self._operators:
            yield k

    def _constructNotifications(self):
        self._notifications = {}
        for v in self._schema['notificationTypes']:
            self._notifications[v['label']] = NotificationType(self, **v)

    def output(self, key):
        for k in self.outputs():
            if k == key:
                return self._output[key]
        raise PyEXception('Output not found: {}'.format(key))

    def outputs(self):
        for k in self._notifications:
            yield k

    def _constructInputs(self):
        self._inputs = {}
        for v in self._schema['schema']:
            self._inputs[v['label']] = Input(self, **v)

    def inputs(self):
        for k in self._inputs:
            yield k

    def input(self, key):
        for k in self.inputs():
            if k == key:
                return self._inputs[key]
        raise PyEXception('Input not found: {}'.format(key))

    def newRule(self, conditions, outputs, additionalKeys=None):
        '''
        Args:
            conditions (List[Condition or List[str]]):    Each condition array will consist of three values; left condition, operator, right condition.
                                            Ex: [ [‘latestPrice’, ‘>’, 200.25], [‘peRatio’, ‘<’, 20] ]

            outputs (List[Output or List[str]]): The object’s schema is defined for each notification type, and is returned by the notificationTypes array in the /rules/schema endpoint.
                                                Every output object will contain method (which should match the value key of the notificationType, and frequency which is the number of seconds to wait between alerts.

                                                Ex: [ { method: ‘webhook’, url: ‘https://myserver.com/iexcloud-webhook’, frequency: 60 } ]

            additionalKeys (List[Input or str]): List of schema data values to be included in alert message in addition to the data values in the conditions.

                                                Ex: ['latestPrice', 'peRatio', 'nextEarningsDate']
        '''
        return Rule(
            self,
            conditions,
            outputs,
            additionalKeys or []
        )

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


class Input(object):
    def __init__(self, label, value, type, scope, isLookup=False, weight=0, weightKey=''):
        self._label = label
        self._value = value
        self._type = type
        self._scope = scope
        self._isLookup = isLookup
        self._weight = weight
        self._weightKey = weightKey


class Operator(object):
    def __init__(self, category, label, value):
        self._category = category
        self._label = label
        self._value = value


class NotificationType(object):
    def __init__(self, label, value, weight, enabled, schema=None):
        self._label = label
        self._value = value
        self._weight = weight
        self._enabled = enabled
        self._schema = schema or {}

    def validate(self):
        try:
            from jsonschema import validate
        except ImportError:
            raise PyEXception('jsonschema package required for schema validation')

        validate(instance=self.toJson(), schema=self._schema)


class Condition(object):
    def __init__(self, left_value, operator, right_value):
        self._left_value = self._constructValue(left_value)
        self._operator = operator
        self._right_value = right_value
        self._validate()

    def _constructValue(self, val):
        if isinstance(val, Input):
            # already fine
            return val
        # TODO

    def _validate(self):
        pass

    def toJson(self):
        return [self._left_value.toString(),
                self._operator.toString(),
                self._right_value.toString()]


class Rule(object):
    def __init__(self, conditions, outputs, additionalKeys=None):
        self._conditions = conditions
        self._outputs = outputs
        self._additionalKeys = additionalKeys or []

    def toJson(self):
        return


class RulesEngine(object):
    def __init__(self, schema, version, token):
        self.reinitialize(schema, version, token)

    def reinitialize(self, schema, version, token):
        self._schema = schema
        self._version = version
        self._token = token
        self._construct()

    def _construct(self):
        self._constructOperators()
        self._constructNotifications()
        self._constructInputs()

    def _constructOperators(self):
        self._operators = {}
        for k, v in self._schema['operators'].items():
            self._operators[k] = [Operator(k, **vv) for vv in v]

    def _constructNotifications(self):
        self._notifications = {}
        for v in self._schema['notificationTypes']:
            self._notifications[v['label']] = NotificationType(**v)

    def _constructInputs(self):
        self._inputs = {}
        for v in self._schema['schema']:
            self._inputs[v['label']] = Input(**v)

# -*- coding: utf-8 -*-
from functools import wraps
from ..common import _getJson, _postJson, _deleteJson, _raiseIfNotStr, PyEXception
from .engine import Rule  # noqa: F401


def lookup(lookup='', token='', version=''):
    '''Pull the latest schema for data points, notification types, and operators used to construct rules.

    https://iexcloud.io/docs/api/#rules-schema

    Args:
        lookup (str): If a schema object has “isLookup”: true, pass the value key to /stable/rules/lookup/{value}. This returns all valid values for the rightValue of a condition.
        token (str): Access token
        version (str): API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(lookup)
    if lookup:
        return _getJson('rules/lookup/{}'.format(lookup), token, version, None)
    return _getJson('rules/schema', token, version, None)


@wraps(lookup)
def schema(token='', version=''):
    return lookup(token=token, version=version)


def create(rule, ruleName, ruleSet, type='any', existingId=None, token='', version=''):
    '''This endpoint is used to both create and edit rules. Note that rules run be default after being created.

    Args:
        rule (Rule or dict): rule object to create
        ruleName (str): name for rule
        ruleSet (str): Valid US symbol or the string ANYEVENT. If the string ANYEVENT is passed, the rule will be triggered for any symbol in the system. The cool down period for alerts (frequency) is applied on a per symbol basis.
        type (str): Specify either any, where if any condition is true you get an alert, or all, where all conditions must be true to trigger an alert. any is the default value
        existingId (Optional[str]): The id of an existing rule only if you are editing the existing rule

    conditions	array	Required An array of arrays. Each condition array will consist of three values; left condition, operator, right condition.

                        Ex: [ [‘latestPrice’, ‘>’, 200.25], [‘peRatio’, ‘<’, 20] ]
    outputs	array	Required An array of one object. The object’s schema is defined for each notification type, and is returned by the notificationTypes array in the /rules/schema endpoint.
                    Every output object will contain method (which should match the value key of the notificationType, and frequency which is the number of seconds to wait between alerts.

                    Ex: [ { method: ‘webhook’, url: ‘https://myserver.com/iexcloud-webhook’, frequency: 60 } ]
    additionalKeys	array	Optional. An array of schema data values to be included in alert message in addition to the data values in the conditions.

                            Ex: ['latestPrice', 'peRatio', 'nextEarningsDate']
    '''
    if type not in ('any', 'all'):
        raise PyEXception('type must be in (any, all). got: {}'.format(type))

    if isinstance(rule, Rule):
        rule = rule.toJson()

    rule['token'] = token
    rule['ruleSet'] = ruleSet
    rule['type'] = type
    rule['ruleName'] = ruleName

    # Conditions, outputs, and additionalKeys handled by rule object
    if 'conditions' not in rule:
        raise PyEXception('rule is missing `conditions` key!')
    if 'outputs' not in rule:
        raise PyEXception('rule is missing `outputs` key!')

    if existingId is not None:
        rule['id'] = existingId
    return _postJson('rules/create', json=rule, token=token, version=version, token_in_params=False)


def pause(ruleId, token='', version=''):
    '''You can control the output of rules by pausing and resume per rule id.

    Args:
        ruleId (str): The id of an existing rule to puase
    '''
    return _postJson('rules/pause', json={"ruleId": ruleId, "token": token}, token=token, version=version, token_in_params=False)


def resume(ruleId, token='', version=''):
    '''You can control the output of rules by pausing and resume per rule id.

    Args:
        ruleId (str): The id of an existing rule to puase
    '''
    return _postJson('rules/resume', json={"ruleId": ruleId, "token": token}, token=token, version=version, token_in_params=False)


def delete(ruleId, token='', version=''):
    '''You can delete a rule by using an __HTTP DELETE__ request. This will stop rule executions and delete the rule from your dashboard. If you only want to temporarily stop a rule, use the pause/resume functionality instead.

    Args:
        ruleId (str): The id of an existing rule to puase
    '''
    return _deleteJson('rules/{}'.format(ruleId), token=token, version=version)


def rule(ruleId, token='', version=''):
    '''Rule information such as the current rule status and execution statistics.

    Args:
        ruleId (str): The id of an existing rule to puase
    '''
    return _getJson('rules/info/{}'.format(ruleId), token=token, version=version)


def rules(token='', version=''):
    '''List all rules that are currently on your account. Each rule object returned will include the current rule status and execution statistics.'''
    return _getJson('rules', token=token, version=version)


def output(ruleId, token='', version=''):
    '''If you choose `logs` as your rule output method, IEX Cloud will save the output objects on our server. You can use this method to retrieve those data objects.

    Args:
        ruleId (str): The id of an existing rule to puase
    '''
    return _getJson('rules/output/{}'.format(ruleId), token=token, version=version)

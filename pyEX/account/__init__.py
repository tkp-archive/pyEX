# -*- coding: utf-8 -*-
import pandas as pd
from functools import wraps
from ..common import _requireSecret, _getJson, _postJson, PyEXception, _USAGE_TYPES


def messageBudget(totalMessages=None, token='', version=''):
    '''Used to set an upper limit, “message budget”, on pay as you go messages where you want to make sure not to go above a certain amount. Set the total messages you wish to consume for the month, and once that limit is reached, all API calls will stop until the limit is removed or increased.

    https://iexcloud.io/docs/api/#message-budget

    Args:
        totalMessages (int): The total messages your account is allowed to consume for the current month above your quota. For example: If your account is allowed 5 million messages, and you do not want to exceed 10 million for the month, then you will pass 10000000 as total messages.
        token (str): Access token
        version (str): API version
    '''
    _requireSecret(token)
    if not isinstance(totalMessages, int):
        raise PyEXception("`totalMessages` must be integer, got {}({})".format(type(totalMessages), totalMessages))
    return _postJson('account/messagebudget?totalMessages={}'.format(totalMessages), token=token, version=version)


def metadata(token='', version=''):
    '''Used to retrieve account details such as current tier, payment status, message quote usage, etc.

    https://iexcloud.io/docs/api/#metadata

    Args:
        token (str): Access token
        version (str): API version

    Returns:
        dict or DataFrame: result
    '''
    _requireSecret(token)
    return _getJson('account/metadata', token, version, None)


@wraps(metadata)
def metadataDF(token='', version=''):
    return pd.DataFrame([metadata(token, version)])


def payAsYouGo(allow=False, token='', version=''):
    '''Used to toggle Pay-as-you-go on your account.

    https://iexcloud.io/docs/api/#pay-as-you-go

    Args:
        allow (bool): Enable or disable pay-as-you-go
        token (str): Access token
        version (str): API version
    '''
    _requireSecret(token)
    if not isinstance(allow, bool):
        raise PyEXception("`allow` must be bool, got {}({})".format(type(allow), allow))
    return _postJson('account/messagebudget?allow={}'.format(allow), token=token, version=version)


def usage(type=None, token='', version=''):
    '''Used to retrieve current month usage for your account.

    https://iexcloud.io/docs/api/#usage

    Args:
        type (Optional[string]): Used to specify which quota to return. Ex: messages, rules, rule-records, alerts, alert-records
        token (str): Access token
        version (str): API version

    Returns:
        dict or DataFrame: result
    '''
    _requireSecret(token)
    if type is not None and type and type not in _USAGE_TYPES:
        raise PyEXception("Type must be in (None, '') or {}".format(_USAGE_TYPES))
    if type:
        return _getJson('account/usage/{}'.format(type), token, version, None)
    return _getJson('account/usage', token, version, None)


@wraps(usage)
def usageDF(type=None, token='', version=''):
    return pd.io.json.json_normalize(usage(type, token, version))

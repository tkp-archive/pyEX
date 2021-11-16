# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import (
    _USAGE_TYPES,
    PyEXception,
    _get,
    _post,
    _getAsync,
    _postAsync,
    _requireSecret,
    json_normalize,
)


def messageBudget(totalMessages=None, token="", version="stable", format="json"):
    """Used to set an upper limit, “message budget”, on pay as you go messages where you want to make sure not to go above a certain amount. Set the total messages you wish to consume for the month, and once that limit is reached, all API calls will stop until the limit is removed or increased.

    https://iexcloud.io/docs/api/#message-budget

    Args:
        totalMessages (int): The total messages your account is allowed to consume for the current month above your quota. For example: If your account is allowed 5 million messages, and you do not want to exceed 10 million for the month, then you will pass 10000000 as total messages.
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json
    """
    _requireSecret(token)
    if not isinstance(totalMessages, int):
        raise PyEXception(
            "`totalMessages` must be integer, got {}({})".format(
                type(totalMessages), totalMessages
            )
        )
    return _post(
        "account/messagebudget?totalMessages={}".format(totalMessages),
        token=token,
        version=version,
        format=format,
    )


@wraps(messageBudget)
async def messageBudgetAsync(
    totalMessages=None, token="", version="stable", format="json"
):
    _requireSecret(token)
    if not isinstance(totalMessages, int):
        raise PyEXception(
            "`totalMessages` must be integer, got {}({})".format(
                type(totalMessages), totalMessages
            )
        )
    return await _postAsync(
        "account/messagebudget?totalMessages={}".format(totalMessages),
        token=token,
        version=version,
        format=format,
    )


def metadata(token="", version="stable", format="json"):
    """Used to retrieve account details such as current tier, payment status, message quote usage, etc.

    https://iexcloud.io/docs/api/#metadata

    Args:
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _requireSecret(token)
    return _get("account/metadata", token=token, version=version, format=format)


@wraps(metadata)
async def metadataAsync(token="", version="stable", format="json"):
    _requireSecret(token)
    return await _getAsync(
        "account/metadata", token=token, version=version, format=format
    )


@wraps(metadata)
def metadataDF(*args, **kwargs):
    return pd.DataFrame([metadata(*args, **kwargs)])


def payAsYouGo(allow=False, token="", version="stable", format="json"):
    """Used to toggle Pay-as-you-go on your account.

    https://iexcloud.io/docs/api/#pay-as-you-go

    Args:
        allow (bool): Enable or disable pay-as-you-go
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json
    """
    _requireSecret(token)
    if not isinstance(allow, bool):
        raise PyEXception("`allow` must be bool, got {}({})".format(type(allow), allow))
    return _post(
        "account/messagebudget?allow={}".format(allow),
        token=token,
        version=version,
        format=format,
    )


@wraps(payAsYouGo)
async def payAsYouGoAsync(allow=False, token="", version="stable", format="json"):
    _requireSecret(token)
    if not isinstance(allow, bool):
        raise PyEXception("`allow` must be bool, got {}({})".format(type(allow), allow))
    return await _postAsync(
        "account/messagebudget?allow={}".format(allow),
        token=token,
        version=version,
        format=format,
    )


def usage(type=None, token="", version="stable", format="json"):
    """Used to retrieve current month usage for your account.

    https://iexcloud.io/docs/api/#usage

    Args:
        type (Optional[string]): Used to specify which quota to return. Ex: messages, rules, rule-records, alerts, alert-records
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _requireSecret(token)
    if type is not None and type and type not in _USAGE_TYPES:
        raise PyEXception("Type must be in (None, '') or {}".format(_USAGE_TYPES))
    if type:
        return _get(
            "account/usage/{}".format(type), token=token, version=version, format=format
        )
    return _get("account/usage", token=token, version=version, format=format)


@wraps(usage)
async def usageAsync(type=None, token="", version="stable", format="json"):
    _requireSecret(token)
    if type is not None and type and type not in _USAGE_TYPES:
        raise PyEXception("Type must be in (None, '') or {}".format(_USAGE_TYPES))
    if type:
        return _getAsync(
            "account/usage/{}".format(type), token=token, version=version, format=format
        )
    return await _getAsync("account/usage", token=token, version=version, format=format)


@wraps(usage)
def usageDF(*args, **kwargs):
    return json_normalize(usage(*args, **kwargs))


def status(token="", version="stable", format="json"):
    """Used to retrieve current system status.

    https://iexcloud.io/docs/api/#status

    Args:
        token (str): Access token
        version (str): API version
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("status", token=token, version=version, format=format)


@wraps(status)
async def statusAsync(token="", version="stable", format="json"):
    return await _getAsync("status", token=token, version=version, format=format)


@wraps(status)
def statusDF(*args, **kwargs):
    return json_normalize(status(*args, **kwargs))

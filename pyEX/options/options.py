# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _getJson, _raiseIfNotStr, _toDatetime


def optionExpirations(symbol, token="", version="", filter=""):
    """Returns end of day options data

    https://iexcloud.io/docs/api/#options
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    return _getJson("stock/" + symbol + "/options", token, version, filter)


def options(symbol, expiration, side="", token="", version="", filter=""):
    """Returns end of day options data

    https://iexcloud.io/docs/api/#options
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (str): Ticker to request
        expiration (str): Expiration date
        side (str): Side (optional)
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    if side:
        return _getJson(
            "stock/{symbol}/options/{expiration}/{side}".format(
                symbol=symbol, expiration=expiration, side=side
            ),
            token,
            version,
            filter,
        )
    return _getJson(
        "stock/{symbol}/options/{expiration}/".format(
            symbol=symbol, expiration=expiration
        ),
        token,
        version,
        filter,
    )


@wraps(options)
def optionsDF(symbol, expiration, side="", token="", version="", filter=""):
    p = options(symbol, expiration, side, token, version, filter)
    df = pd.DataFrame(p)
    _toDatetime(df, tcols=["date"])
    return df

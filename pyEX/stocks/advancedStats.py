# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

from ..common import (
    _EST,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _toDatetime,
    json_normalize,
)


@_expire(hour=4, tz=_EST)
def advancedStats(symbol, token="", version="stable", filter="", format="json"):
    """Returns everything in key stats plus additional advanced stats such as EBITDA, ratios, key financial data, and more.

    https://iexcloud.io/docs/api/#advanced-stats
    4am, 5am ET

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    return _get(
        "stock/{symbol}/advanced-stats".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(advancedStats)
def advancedStatsDF(*args, **kwargs):
    return _toDatetime(json_normalize(advancedStats(*args, **kwargs)))

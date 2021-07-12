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
    _EST,
    _UTC,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _toDatetime,
    json_normalize,
)


@_expire(hour=4, tz=_UTC)
def marketYesterday(token="", version="stable", filter="", format="json"):
    """This returns previous day adjusted price data for whole market

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/previous", token, version, filter)


marketPrevious = marketYesterday


@wraps(marketYesterday)
def marketYesterdayDF(*args, **kwargs):
    x = marketYesterday(*args, **kwargs)
    data = []
    for key in x:
        data.append(x[key])
        data[-1]["symbol"] = key
    return _reindex(_toDatetime(pd.DataFrame(data)), "symbol")


marketPreviousDF = marketYesterdayDF


@_expire(hour=4, tz=_EST)
def yesterday(symbol, token="", version="stable", filter="", format="json"):
    """This returns previous day adjusted price data for one or more stocks

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

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
        "stock/{symbol}/previous".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


previous = yesterday


@wraps(yesterday)
def yesterdayDF(*args, **kwargs):
    y = yesterday(*args, **kwargs)
    if y:
        df = _reindex(_toDatetime(json_normalize(y)), "symbol")
    else:
        df = pd.DataFrame()
    return df


previousDF = yesterdayDF

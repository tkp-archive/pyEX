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
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _toDatetime,
    json_normalize,
)


def marketOhlc(token="", version="stable", filter="", format="json"):
    """Returns the official open and close for whole market.

    https://iexcloud.io/docs/api/#news
    9:30am-5pm ET Mon-Fri

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/ohlc", token, version, filter)


@wraps(marketOhlc)
def marketOhlcDF(*args, **kwargs):
    x = marketOhlc(*args, **kwargs)
    data = []
    for key in x:
        data.append(x[key])
        data[-1]["symbol"] = key
    return _reindex(_toDatetime(json_normalize(data)), "symbol")


def ohlc(symbol, token="", version="stable", filter="", format="json"):
    """Returns the official open and close for a give symbol.

    https://iexcloud.io/docs/api/#ohlc
    9:30am-5pm ET Mon-Fri

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
        "stock/{symbol}/ohlc".format(symbol=_quoteSymbols(symbol)) + symbol + "/ohlc",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(ohlc)
def ohlcDF(*args, **kwargs):
    o = ohlc(*args, **kwargs)
    if o:
        df = json_normalize(o)
        _toDatetime(df)
    else:
        df = pd.DataFrame()
    return df

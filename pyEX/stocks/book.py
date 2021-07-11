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
    _toDatetime,
    json_normalize,
)


def book(symbol, token="", version="stable", filter="", format="json"):
    """Book data

    https://iextrading.com/developer/docs/#book
    realtime during Investors Exchange market hours

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
    symbol = _quoteSymbols(symbol)
    return _get(
        "stock/{symbol}/book".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def _bookToDF(b):
    """internal"""
    quote = b.get("quote", [])
    asks = b.get("asks", [])
    bids = b.get("bids", [])
    trades = b.get("trades", [])

    df1 = json_normalize(quote)
    df1["type"] = "quote"

    df2 = json_normalize(asks)
    df2["symbol"] = quote["symbol"]
    df2["type"] = "ask"

    df3 = json_normalize(bids)
    df3["symbol"] = quote["symbol"]
    df3["type"] = "bid"

    df4 = json_normalize(trades)
    df4["symbol"] = quote["symbol"]
    df3["type"] = "trade"

    df = pd.concat([df1, df2, df3, df4], sort=True)
    _toDatetime(df)
    return df


@wraps(book)
def bookDF(*args, **kwargs):
    return _bookToDF(book(*args, **kwargs))

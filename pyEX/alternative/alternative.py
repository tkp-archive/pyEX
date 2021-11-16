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
    _getAsync,
    _raiseIfNotStr,
    _strOrDate,
    _toDatetime,
)


def sentiment(
    symbol,
    type="daily",
    date=None,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This endpoint provides social sentiment data from StockTwits. Data can be viewed as a daily value, or by minute for a given date.

    https://iexcloud.io/docs/api/#social-sentiment
    Continuous

    Args:
        symbol (str): Ticker to request
        type (str): 'daily' or 'minute'
        date (str): date in YYYYMMDD or datetime
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    if date:
        date = _strOrDate(date)
        return _get(
            "stock/{symbol}/sentiment/{type}/{date}".format(
                symbol=symbol, type=type, date=date
            ),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "stock/{symbol}/sentiment/{type}/".format(symbol=symbol, type=type),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(sentiment)
async def sentimentAsync(
    symbol,
    type="daily",
    date=None,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This endpoint provides social sentiment data from StockTwits. Data can be viewed as a daily value, or by minute for a given date.

    https://iexcloud.io/docs/api/#social-sentiment
    Continuous

    Args:
        symbol (str): Ticker to request
        type (str): 'daily' or 'minute'
        date (str): date in YYYYMMDD or datetime
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    if date:
        date = _strOrDate(date)
        return _get(
            "stock/{symbol}/sentiment/{type}/{date}".format(
                symbol=symbol, type=type, date=date
            ),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return await _getAsync(
        "stock/{symbol}/sentiment/{type}/".format(symbol=symbol, type=type),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(sentiment)
def sentimentDF(*args, **kwargs):
    ret = sentiment(*args, **kwargs)
    if type == "daily":
        ret = [ret]
    return _toDatetime(pd.DataFrame(ret))

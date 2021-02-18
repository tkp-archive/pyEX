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
    _expire,
    _get,
    _raiseIfNotStr,
    _reindex,
    _strOrDate,
    _toDatetime,
    json_normalize,
)


def crypto(token="", version="", filter=""):
    """This will return an array of quotes for all Cryptocurrencies supported by the IEX API. Each element is a standard quote object with four additional keys.

    https://iexcloud.io/docs/api/#crypto

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/crypto/", token, version, filter)


@wraps(crypto)
def cryptoDF(token="", version="", filter=""):
    df = pd.DataFrame(crypto(token, version, filter))
    _toDatetime(df)
    _reindex(df, "symbol")
    return df


def sentiment(
    symbol, type="daily", date=None, token="", version="", filter="", format="json"
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
def sentimentDF(*args, **kwargs):
    ret = sentiment(*args, **kwargs)
    if type == "daily":
        ret = [ret]
    return _toDatetime(pd.DataFrame(ret))


@_expire(hour=1)
def ceoCompensation(symbol, token="", version="", filter=""):
    """This endpoint provides CEO compensation for a company by symbol.

    https://iexcloud.io/docs/api/#ceo-compensation
    1am daily

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
        "stock/{symbol}/ceo-compensation".format(symbol=symbol), token, version, filter
    )


@wraps(ceoCompensation)
def ceoCompensationDF(*args, **kwargs):
    return _toDatetime(json_normalize(ceoCompensation(*args, **kwargs)))

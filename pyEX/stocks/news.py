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
    _interval,
)


@_interval(minutes=5)
def news(
    symbol,
    last=10,
    language="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """News about company

    https://iexcloud.io/docs/api/#news
    Continuous

    Args:
        symbol (str): Ticker to request
        last (int): limit number of results
        langauge (str): filter results by language
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
        dict: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    url = "/stock/{}/news/last/{}".format(symbol, last)
    if language:
        url += "?language={}".format(language)
    return _get(url, token, version, filter)


def _newsToDF(n):
    """internal"""
    return _reindex(_toDatetime(pd.DataFrame(n), reformatcols=["datetime"]), "datetime")


@wraps(news)
def newsDF(*args, **kwargs):
    return _newsToDF(news(*args, **kwargs))


def marketNews(
    last=10, language="", token="", version="stable", filter="", format="json"
):
    """News about market

    https://iexcloud.io/docs/api/#news
    Continuous

    Args:
        last (int): limit number of results
        langauge (str): filter results by language
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
        dict: result
    """
    url = "/stock/market/news/last/{}".format(last)
    if language:
        url += "?language={}".format(language)

    return _get(
        url,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(marketNews)
def marketNewsDF(*args, **kwargs):
    return _reindex(_toDatetime(pd.DataFrame(marketNews(*args, **kwargs))), "datetime")

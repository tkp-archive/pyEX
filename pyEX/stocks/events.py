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


def upcomingEvents(
    symbol="",
    exactDate="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This will return all upcoming estimates, dividends, splits for a given symbol or the market. If market is passed for the symbol, IPOs will also be included.

    https://iexcloud.io/docs/api/#upcoming-events

    Args:
        symbol (str): Symbol to look up
        exactDate (str): exactDate Optional. Exact date for which to get data
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result

    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)

    if symbol:
        url = "stock/{}/upcoming-events".format(symbol)
    else:
        url = "stock/market/upcoming-events"

    if exactDate:
        url += "?exactDate={}".format(exactDate)
    return _get(url, token, version, filter)


def _upcomingToDF(upcoming):
    dfs = {}
    for k, v in upcoming.items():
        dfs[k] = _toDatetime(pd.DataFrame(v))
    return dfs


@wraps(upcomingEvents)
def upcomingEventsDF(*args, **kwargs):
    return _upcomingToDF(upcomingEvents(*args, **kwargs))


def upcomingEarnings(
    symbol="",
    exactDate="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This will return all upcoming estimates, dividends, splits for a given symbol or the market. If market is passed for the symbol, IPOs will also be included.

    https://iexcloud.io/docs/api/#upcoming-events

    Args:
        symbol (str): Symbol to look up
        exactDate (str): exactDate Optional. Exact date for which to get data
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result

    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    if symbol:
        url = "stock/{}/upcoming-earnings".format(symbol)
    else:
        url = "stock/market/upcoming-earnings"

    if exactDate:
        url += "?exactDate={}".format(exactDate)
    return _get(url, token, version, filter)


@wraps(upcomingEarnings)
def upcomingEarningsDF(*args, **kwargs):
    return json_normalize(upcomingEarnings(*args, **kwargs))


def upcomingDividends(
    symbol="",
    exactDate="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This will return all upcoming estimates, dividends, splits for a given symbol or the market. If market is passed for the symbol, IPOs will also be included.

    https://iexcloud.io/docs/api/#upcoming-events

    Args:
        symbol (str): Symbol to look up
        exactDate (str): exactDate Optional. Exact date for which to get data
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result

    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    if symbol:
        url = "stock/{}/upcoming-dividends".format(symbol)
    else:
        url = "stock/market/upcoming-dividends"

    if exactDate:
        url += "?exactDate={}".format(exactDate)
    return _get(url, token, version, filter)


@wraps(upcomingDividends)
def upcomingDividendsDF(*args, **kwargs):
    return json_normalize(upcomingDividends(*args, **kwargs))


def upcomingSplits(
    symbol="",
    exactDate="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This will return all upcoming estimates, dividends, splits for a given symbol or the market. If market is passed for the symbol, IPOs will also be included.

    https://iexcloud.io/docs/api/#upcoming-events

    Args:
        symbol (str): Symbol to look up
        exactDate (str): exactDate Optional. Exact date for which to get data
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result

    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    if symbol:
        url = "stock/{}/upcoming-splits".format(symbol)
    else:
        url = "stock/market/upcoming-splits"

    if exactDate:
        url += "?exactDate={}".format(exactDate)
    return _get(url, token, version, filter)


@wraps(upcomingSplits)
def upcomingSplitsDF(*args, **kwargs):
    return json_normalize(upcomingSplits(*args, **kwargs))


def upcomingIPOs(
    symbol="",
    exactDate="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This will return all upcoming estimates, dividends, splits for a given symbol or the market. If market is passed for the symbol, IPOs will also be included.

    https://iexcloud.io/docs/api/#upcoming-events

    Args:
        symbol (str): Symbol to look up
        exactDate (str): exactDate Optional. Exact date for which to get data
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result

    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    if symbol:
        url = "stock/{}/upcoming-ipos".format(symbol)
    else:
        url = "stock/market/upcoming-ipos"

    if exactDate:
        url += "?exactDate={}".format(exactDate)
    return _get(url, token, version, filter)


@wraps(upcomingIPOs)
def upcomingIPOsDF(*args, **kwargs):
    return json_normalize(upcomingIPOs(*args, **kwargs))

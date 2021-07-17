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
    _strToList,
    _quoteSymbols,
    _toDatetime,
    json_normalize,
)


def _baseEvent(
    event="events",
    symbol="",
    exactDate="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    symbol = _strToList(symbol)

    if len(symbol) == 0:
        # full market
        url = "stock/market/upcoming-{}".format(event)
    elif len(symbol) == 1:
        # just 1 symbol
        url = "stock/{}/upcoming-{}".format(_quoteSymbols(symbol), event)
    else:
        # many symbols
        url = "stock/market/upcoming-{}?symbols={}".format(event, _quoteSymbols(symbol))

    if exactDate and len(symbol) > 1:
        url += "&exactDate={}".format(exactDate)
    elif exactDate:
        url += "?exactDate={}".format(exactDate)

    return _get(url, token, version, filter)


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
    return _baseEvent(
        "events",
        symbol=symbol,
        exactDate=exactDate,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


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
    return _baseEvent(
        "earnings",
        symbol=symbol,
        exactDate=exactDate,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


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
    return _baseEvent(
        "dividends",
        symbol=symbol,
        exactDate=exactDate,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


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
    return _baseEvent(
        "splits",
        symbol=symbol,
        exactDate=exactDate,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


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
    return _baseEvent(
        "ipos",
        symbol=symbol,
        exactDate=exactDate,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(upcomingIPOs)
def upcomingIPOsDF(*args, **kwargs):
    return json_normalize(upcomingIPOs(*args, **kwargs))

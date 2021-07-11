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
    _UTC,
    _checkPeriodLast,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _toDatetime,
    json_normalize,
)


@_expire(hour=9, tz=_UTC)
def earnings(
    symbol,
    period="quarter",
    last=1,
    field="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Earnings data for a given company including the actual EPS, consensus, and fiscal period. Earnings are available quarterly (last 4 quarters) and annually (last 4 years).

    https://iexcloud.io/docs/api/#earnings
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        field (str): Subfield to fetch
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _checkPeriodLast(period, last)
    if not field:
        return _get(
            "stock/{}/earnings?period={}&last={}".format(symbol, period, last),
            token=token,
            version=version,
            filter=filter,
            format=format,
        ).get("earnings", [])
    return _get(
        "stock/{}/earnings/{}/{}?period={}".format(symbol, last, field, period),
        token=token,
        version=version,
        filter=filter,
        format=format,
    ).get("earnings", [])


def _earningsToDF(e):
    """internal"""
    if e:
        df = _reindex(_toDatetime(pd.DataFrame(e)), "EPSReportDate")
    else:
        df = pd.DataFrame()
    return df


@wraps(earnings)
def earningsDF(*args, **kwargs):
    return _earningsToDF(earnings(*args, **kwargs))


@_expire(minute=0)
def earningsToday(token="", version="stable", filter="", format="json"):
    """Returns earnings that will be reported today as two arrays: before the open bto and after market close amc.
    Each array contains an object with all keys from earnings, a quote object, and a headline key.

    https://iexcloud.io/docs/api/#earnings-today
    Updates at 9am, 11am, 12pm UTC daily


    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/today-earnings", token, version, filter)


@wraps(earningsToday)
def earningsTodayDF(*args, **kwargs):
    x = earningsToday(*args, **kwargs)
    z = []
    for k in x:
        ds = x[k]
        for d in ds:
            d["when"] = k
            z.extend(ds)
    df = json_normalize(z)

    if not df.empty:
        df.drop_duplicates(inplace=True)
    return _reindex(_toDatetime(df), "symbol")


@_expire(hour=10, tz=_UTC)
def ipoToday(token="", version="stable", filter="", format="json"):
    """This returns a list of upcoming or today IPOs scheduled for the current and next month. The response is split into two structures:
    rawData and viewData. rawData represents all available data for an IPO. viewData represents data structured for display to a user.

    https://iexcloud.io/docs/api/#ipo-calendar
    10am, 10:30am UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/today-ipos", token, version, filter)


@wraps(ipoToday)
def ipoTodayDF(*args, **kwargs):
    val = ipoToday(*args, **kwargs)
    if val:
        df = _reindex(_toDatetime(json_normalize(val, "rawData")), "symbol")
    else:
        df = pd.DataFrame()
    return df


@_expire(hour=10)
def ipoUpcoming(token="", version="stable", filter="", format="json"):
    """This returns a list of upcoming or today IPOs scheduled for the current and next month. The response is split into two structures:
    rawData and viewData. rawData represents all available data for an IPO. viewData represents data structured for display to a user.

    https://iexcloud.io/docs/api/#ipo-calendar
    10am, 10:30am UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/upcoming-ipos", token, version, filter)


@wraps(ipoUpcoming)
def ipoUpcomingDF(*args, **kwargs):
    val = ipoUpcoming(*args, **kwargs)
    if val:
        df = _reindex(_toDatetime(json_normalize(val, "rawData")), "symbol")
    else:
        df = pd.DataFrame()
    return df


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

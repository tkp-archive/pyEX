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
    _COLLECTION_TAGS,
    _EST,
    _LIST_OPTIONS,
    _UTC,
    PyEXception,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _strOrDate,
    _toDatetime,
    json_normalize,
)


@_expire(hour=0)
def collections(
    tag,
    collectionName,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Returns an array of quote objects for a given collection type. Currently supported collection types are sector, tag, and list


    https://iexcloud.io/docs/api/#collections

    Args:
        tag (str):  Sector, Tag, or List
        collectionName (str):  Associated name for tag
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    if tag not in _COLLECTION_TAGS:
        raise PyEXception("Tag must be in %s" % str(_COLLECTION_TAGS))
    return _get(
        "stock/market/collection/" + tag + "?collectionName=" + collectionName,
        token,
        version,
        filter,
    )


@wraps(collections)
def collectionsDF(*args, **kwargs):
    return _reindex(_toDatetime(pd.DataFrame(collections(*args, **kwargs))), "symbol")


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


def list(
    option="mostactive",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Returns an array of quotes for the top 10 symbols in a specified list.


    https://iexcloud.io/docs/api/#list
    Updated intraday

    Args:
        option (str): Option to query
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    if option not in _LIST_OPTIONS:
        raise PyEXception("Option must be in %s" % str(_LIST_OPTIONS))
    return _get("stock/market/list/" + option, token, version, filter)


@wraps(list)
def listDF(*args, **kwargs):
    return _reindex(_toDatetime(pd.DataFrame(list(*args, **kwargs))), "symbol")


def marketVolume(token="", version="stable", filter="", format="json"):
    """This endpoint returns real time traded volume on U.S. markets.

    https://iexcloud.io/docs/api/#market-volume-u-s
    7:45am-5:15pm ET Mon-Fri

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("market/", token, version, filter)


@wraps(marketVolume)
def marketVolumeDF(token="", version="stable", filter="", format="json"):
    df = pd.DataFrame(marketVolume())
    _toDatetime(df, cols=[], tcols=["lastUpdated"])
    return df


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


def sectorPerformance(token="", version="stable", filter="", format="json"):
    """This returns an array of each sector and performance for the current trading day. Performance is based on each sector ETF.

    https://iexcloud.io/docs/api/#sector-performance
    8am-5pm ET Mon-Fri

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/sector-performance", token, version, filter)


@wraps(sectorPerformance)
def sectorPerformanceDF(*args, **kwargs):
    return _reindex(
        _toDatetime(
            pd.DataFrame(sectorPerformance(*args, **kwargs)),
            cols=[],
            tcols=["lastUpdated"],
        ),
        "name",
    )


@_expire(hour=16, tz=_EST)
def marketShortInterest(
    date=None, token="", version="stable", filter="", format="json"
):
    """The consolidated market short interest positions in all IEX-listed securities are included in the IEX Short Interest Report.

    The report data will be published daily at 4:00pm ET.

    https://iexcloud.io/docs/api/#listed-short-interest-list-in-dev

    Args:
        date (datetime): Effective Datetime
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    if date:
        date = _strOrDate(date)
        return _get("stock/market/short-interest/" + date, token, version, filter)
    return _get("stock/market/short-interest", token, version, filter)


@wraps(marketShortInterest)
def marketShortInterestDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(marketShortInterest(*args, **kwargs)))


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

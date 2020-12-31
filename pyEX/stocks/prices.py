# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import (
    _EST,
    _TIMEFRAME_CHART,
    PyEXception,
    _expire,
    _getJson,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _strOrDate,
    _toDatetime,
    json_normalize,
)


def book(symbol, token="", version="", filter=""):
    """Book data

    https://iextrading.com/developer/docs/#book
    realtime during Investors Exchange market hours

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    return _getJson("stock/" + symbol + "/book", token, version, filter)


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
def bookDF(symbol, token="", version="", filter=""):
    x = book(symbol, token, version, filter)
    df = _bookToDF(x)
    return df


# @_expire(hour=4, tz=_EST)
def chart(
    symbol,
    timeframe="1m",
    date=None,
    exactDate=None,
    last=-1,
    closeOnly=False,
    byDay=False,
    simplify=False,
    interval=-1,
    changeFromClose=False,
    displayPercent=False,
    sort="desc",
    includeToday=False,
    token="",
    version="",
    filter="",
):
    """Historical price/volume data, daily and intraday

    https://iexcloud.io/docs/api/#historical-prices
    Data Schedule
    1d: -9:30-4pm ET Mon-Fri on regular market trading days
        -9:30-1pm ET on early close trading days
    All others:
        -Prior trading day available after 4am ET Tue-Sat

    Args:
        symbol (str): Ticker to request
        timeframe (str): Timeframe to request e.g. 1m
        date (datetime): date, if requesting intraday
        exactDate (str): Same as `date`, takes precedence
        last (int): If passed, chart data will return the last N elements from the time period defined by the range parameter
        closeOnly (bool): Will return adjusted data only with keys date, close, and volume.
        byDay (bool): Used only when range is date to return OHLCV data instead of minute bar data.
        simplify (bool) If true, runs a polyline simplification using the Douglas-Peucker algorithm. This is useful if plotting sparkline charts.
        interval (int) If passed, chart data will return every Nth element as defined by chartInterval
        changeFromClose (bool): If true, changeOverTime and marketChangeOverTime will be relative to previous day close instead of the first value.
        displayPercent (bool): If set to true, all percentage values will be multiplied by a factor of 100 (Ex: /stock/twtr/chart?displayPercent=true)
        range (str): Same format as the path parameter. This can be used for batch calls.
        sort (str): Can be "asc" or "desc" to sort results by date. Defaults to "desc"
        includeToday (bool): If true, current trading day data is appended
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)

    base_url = "stock/{}/chart/{}?".format(symbol, timeframe)

    # exactDate takes precedence
    date = exactDate or date
    if date:
        date = _strOrDate(date)

    if timeframe is not None and timeframe != "1d":
        if timeframe not in _TIMEFRAME_CHART:
            raise PyEXception("Range must be in {}".format(_TIMEFRAME_CHART))

    # Assemble params
    params = {}

    # TODO need these?
    # if date:
    #     params["exactDate"] = date
    # if range:
    #     params["range"] = range

    if last > 0:
        params["chartLast"] = last

    if closeOnly:
        params["chartCloseOnly"] = closeOnly

    if byDay:
        params["chartByDay"] = byDay

    if simplify:
        params["chartSimplify"] = simplify

    if interval > 0:
        params["chartInterval"] = interval

    if changeFromClose:
        params["changeFromClose"] = changeFromClose

    if displayPercent:
        params["displayPercent"] = displayPercent

    if exactDate:
        params["exactDate"] = exactDate

    if sort:
        if sort.lower() not in (
            "asc",
            "desc",
        ):
            raise PyEXception("Sort must be in (asc, desc), got: {}".format(sort))

        params["sort"] = sort.lower()

    if includeToday:
        params["includeToday"] = includeToday

    if date:
        base_url = "stock/{}/chart/date/{}?".format(symbol, date)

        if params:
            base_url += "&".join("{}={}".format(k, v) for k, v in params.items())
        return _getJson(base_url, token, version, filter)

    if params:
        base_url += "&".join("{}={}".format(k, v) for k, v in params.items())

    return _getJson(base_url, token, version, filter)


def _chartToDF(c):
    """internal"""
    df = pd.DataFrame(c)
    _toDatetime(df)
    _reindex(df, "date")
    return df


@wraps(chart)
def chartDF(
    symbol,
    timeframe="1m",
    date=None,
    exactDate=None,
    last=-1,
    closeOnly=False,
    byDay=False,
    simplify=False,
    interval=-1,
    changeFromClose=False,
    displayPercent=False,
    sort="desc",
    includeToday=False,
    token="",
    version="",
    filter="",
):
    c = chart(
        symbol=symbol,
        timeframe=timeframe,
        date=date,
        exactDate=exactDate,
        last=last,
        closeOnly=closeOnly,
        byDay=byDay,
        simplify=simplify,
        interval=interval,
        changeFromClose=changeFromClose,
        displayPercent=displayPercent,
        sort=sort,
        includeToday=includeToday,
        token=token,
        version=version,
        filter=filter,
    )
    df = pd.DataFrame(c)
    _toDatetime(df)
    if timeframe is not None and timeframe != "1d":
        _reindex(df, "date")
    else:
        if not df.empty and "date" in df.columns and "minute" in df.columns:
            df.set_index(["date", "minute"], inplace=True)
        elif not df.empty and "date" in df.columns:
            _reindex(df, "date")
        elif not df.empty:
            # Nothing to do
            ...
        else:
            df = pd.DataFrame()
    return df


@_expire(second=0)
def delayedQuote(symbol, token="", version="", filter=""):
    """This returns the 15 minute delayed market quote.

    https://iexcloud.io/docs/api/#delayed-quote
    15min delayed
    4:30am - 8pm ET M-F when market is open

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    return _getJson("stock/" + symbol + "/delayed-quote", token, version, filter)


@wraps(delayedQuote)
def delayedQuoteDF(symbol, token="", version="", filter=""):
    df = json_normalize(delayedQuote(symbol, token, version, filter))
    _toDatetime(df)
    _reindex(df, "symbol")
    return df


def intraday(
    symbol,
    date="",
    exactDate="",
    last=-1,
    IEXOnly=False,
    reset=False,
    simplify=False,
    interval=-1,
    changeFromClose=False,
    IEXWhenNull=False,
    token="",
    version="",
    filter="",
):
    """This endpoint will return aggregated intraday prices in one minute buckets

    https://iexcloud.io/docs/api/#intraday-prices
    9:30-4pm ET Mon-Fri on regular market trading days
    9:30-1pm ET on early close trading days

    Args:
        symbol (str): Ticker to request
        date (str): Formatted as YYYYMMDD. This can be used for batch calls when range is 1d or date. Currently supporting trailing 30 calendar days of minute bar data.
        exactDate (str): Same as `date`, takes precedence
        last (number): If passed, chart data will return the last N elements
        IEXOnly (bool): Limits the return of intraday prices to IEX only data.
        reset (bool): If true, chart will reset at midnight instead of the default behavior of 9:30am ET.
        simplify (bool): If true, runs a polyline simplification using the Douglas-Peucker algorithm. This is useful if plotting sparkline charts.
        interval (number): If passed, chart data will return every Nth element as defined by chartInterval
        changeFromClose (bool): If true, changeOverTime and marketChangeOverTime will be relative to previous day close instead of the first value.
        IEXWhenNull (bool): By default, all market prefixed fields are 15 minute delayed, meaning the most recent 15 objects will be null. If this parameter is passed as true, all market prefixed fields that are null will be populated with IEX data if available.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)

    # exactDate takes precedence
    date = exactDate or date
    if date:
        date = _strOrDate(date)

    # Assemble params
    params = {}

    if date:
        params["exactDate"] = date

    if last > 0:
        params["chartLast"] = last

    if IEXOnly:
        params["chartIEXOnly"] = IEXOnly

    if reset:
        params["chartReset"] = reset

    if simplify:
        params["chartSimplify"] = simplify

    if interval > 0:
        params["chartInterval"] = interval

    if changeFromClose:
        params["changeFromClose"] = changeFromClose

    if IEXWhenNull:
        params["chartIEXWhenNull"] = IEXWhenNull

    base_url = "stock/{}/intraday-prices?".format(symbol)

    if params:
        base_url += "&".join("{}={}".format(k, v) for k, v in params.items())
    return _getJson(base_url, token, version, filter)


@wraps(intraday)
def intradayDF(
    symbol,
    date="",
    exactDate="",
    last=-1,
    IEXOnly=False,
    reset=False,
    simplify=False,
    interval=-1,
    changeFromClose=False,
    IEXWhenNull=False,
    token="",
    version="",
    filter="",
):
    val = intraday(
        symbol=symbol,
        date=date,
        exactDate=exactDate,
        last=last,
        IEXOnly=IEXOnly,
        reset=reset,
        simplify=simplify,
        interval=interval,
        changeFromClose=changeFromClose,
        IEXWhenNull=IEXWhenNull,
        token=token,
        version=version,
        filter=filter,
    )
    df = pd.DataFrame(val)
    _toDatetime(df)
    if not df.empty and "date" in df.columns and "minute" in df.columns:
        df.set_index(["date", "minute"], inplace=True)
    elif not df.empty and "date" in df.columns:
        _reindex(df, "date")
    else:
        df = pd.DataFrame()
    return df


def largestTrades(symbol, token="", version="", filter=""):
    """This returns 15 minute delayed, last sale eligible trades.

    https://iexcloud.io/docs/api/#largest-trades
    9:30-4pm ET M-F during regular market hours

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    return _getJson("stock/" + symbol + "/largest-trades", token, version, filter)


@wraps(largestTrades)
def largestTradesDF(symbol, token="", version="", filter=""):
    df = pd.DataFrame(largestTrades(symbol, token, version, filter))
    _toDatetime(df)
    _reindex(df, "time")
    return df


def ohlc(symbol, token="", version="", filter=""):
    """Returns the official open and close for a give symbol.

    https://iexcloud.io/docs/api/#news
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    return _getJson("stock/" + symbol + "/ohlc", token, version, filter)


@wraps(ohlc)
def ohlcDF(symbol, token="", version="", filter=""):
    o = ohlc(symbol, token, version, filter)
    if o:
        df = json_normalize(o)
        _toDatetime(df)
    else:
        df = pd.DataFrame()
    return df


@_expire(hour=4, tz=_EST)
def yesterday(symbol, token="", version="", filter=""):
    """This returns previous day adjusted price data for one or more stocks

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    return _getJson("stock/" + symbol + "/previous", token, version, filter)


previous = yesterday


@wraps(yesterday)
def yesterdayDF(symbol, token="", version="", filter=""):
    y = yesterday(symbol, token, version, filter)
    if y:
        df = json_normalize(y)
        _toDatetime(df)
        _reindex(df, "symbol")
    else:
        df = pd.DataFrame()
    return df


previousDF = yesterdayDF


def price(symbol, token="", version="", filter=""):
    """Price of ticker

    https://iexcloud.io/docs/api/#price
    4:30am-8pm ET Mon-Fri

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    return _getJson("stock/" + symbol + "/price", token, version, filter)


@wraps(price)
def priceDF(symbol, token="", version="", filter=""):
    df = json_normalize({"price": price(symbol, token, version, filter)})
    _toDatetime(df)
    return df


def quote(symbol, token="", version="", filter=""):
    """Get quote for ticker

    https://iexcloud.io/docs/api/#quote
    4:30am-8pm ET Mon-Fri


    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    return _getJson("stock/" + symbol + "/quote", token, version, filter)


@wraps(quote)
def quoteDF(symbol, token="", version="", filter=""):
    q = quote(symbol, token, version, filter)
    if q:
        df = json_normalize(q)
        _toDatetime(df)
        _reindex(df, "symbol")
    else:
        df = pd.DataFrame()
    return df


@_expire(hour=8, tz=_EST)
def spread(symbol, token="", version="", filter=""):
    """This returns an array of effective spread, eligible volume, and price improvement of a stock, by market.
    Unlike volume-by-venue, this will only return a venue if effective spread is not ‘N/A’. Values are sorted in descending order by effectiveSpread.
    Lower effectiveSpread and higher priceImprovement values are generally considered optimal.

    Effective spread is designed to measure marketable orders executed in relation to the market center’s
    quoted spread and takes into account hidden and midpoint liquidity available at each market center.
    Effective Spread is calculated by using eligible trade prices recorded to the consolidated tape and
    comparing those trade prices to the National Best Bid and Offer (“NBBO”) at the time of the execution.

    View the data disclaimer at the bottom of the stocks app for more information about how these values are calculated.


    https://iexcloud.io/docs/api/#earnings-today
    8am ET M-F

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    return _getJson("stock/" + symbol + "/effective-spread", token, version, filter)


@wraps(spread)
def spreadDF(symbol, token="", version="", filter=""):
    df = pd.DataFrame(spread(symbol, token, version, filter))
    _toDatetime(df)
    _reindex(df, "venue")
    return df


def volumeByVenue(symbol, token="", version="", filter=""):
    """This returns 15 minute delayed and 30 day average consolidated volume percentage of a stock, by market.
    This call will always return 13 values, and will be sorted in ascending order by current day trading volume percentage.

    https://iexcloud.io/docs/api/#volume-by-venue
    Updated during regular market hours 9:30am-4pm ET


    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    return _getJson("stock/" + symbol + "/volume-by-venue", token, version, filter)


@wraps(volumeByVenue)
def volumeByVenueDF(symbol, token="", version="", filter=""):
    df = pd.DataFrame(volumeByVenue(symbol, token, version, filter))
    _toDatetime(df)
    _reindex(df, "venue")
    return df

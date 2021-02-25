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
    _EST,
    _TIMEFRAME_CHART,
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


@_expire(hour=4, tz=_EST)
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
    version="stable",
    filter="",
    format="json",
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
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)

    base_url = "stock/{}/chart/{}?".format(_quoteSymbols(symbol), timeframe)

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
        base_url = "stock/{}/chart/date/{}?".format(_quoteSymbols(symbol), date)

        if params:
            base_url += "&".join("{}={}".format(k, v) for k, v in params.items())
        return _get(
            base_url, token=token, version=version, filter=filter, format=format
        )

    if params:
        base_url += "&".join("{}={}".format(k, v) for k, v in params.items())

    return _get(base_url, token=token, version=version, filter=filter, format=format)


def _chartToDF(c):
    """internal"""
    return _reindex(_toDatetime(pd.DataFrame(c)), "date")


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
    version="stable",
    filter="",
    format="json",
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
        format=format,
    )
    df = _toDatetime(pd.DataFrame(c))
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
def delayedQuote(symbol, token="", version="stable", filter="", format="json"):
    """This returns the 15 minute delayed market quote.

    https://iexcloud.io/docs/api/#delayed-quote
    15min delayed
    4:30am - 8pm ET M-F when market is open

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
        "stock/{symbol}/delayed-quote".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(delayedQuote)
def delayedQuoteDF(*args, **kwargs):
    return _reindex(
        _toDatetime(json_normalize(delayedQuote(*args, **kwargs))), "symbol"
    )


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
    version="stable",
    filter="",
    format="json",
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
        format (str): return format, defaults to json

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
    return _get(base_url, token=token, version=version, filter=filter, format=format)


@wraps(intraday)
def intradayDF(*args, **kwargs):
    val = intraday(*args, **kwargs)
    df = _toDatetime(pd.DataFrame(val))
    if not df.empty and "date" in df.columns and "minute" in df.columns:
        df.set_index(["date", "minute"], inplace=True)
    elif not df.empty and "date" in df.columns:
        _reindex(df, "date")
    else:
        df = pd.DataFrame()
    return df


def largestTrades(symbol, token="", version="stable", filter="", format="json"):
    """This returns 15 minute delayed, last sale eligible trades.

    https://iexcloud.io/docs/api/#largest-trades
    9:30-4pm ET M-F during regular market hours

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
        "stock/{symbol}/largest-trades".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(largestTrades)
def largestTradesDF(*args, **kwargs):
    return _reindex(_toDatetime(pd.DataFrame(largestTrades(*args, **kwargs))), "time")


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


@_expire(hour=4, tz=_EST)
def yesterday(symbol, token="", version="stable", filter="", format="json"):
    """This returns previous day adjusted price data for one or more stocks

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

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
        "stock/{symbol}/previous".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


previous = yesterday


@wraps(yesterday)
def yesterdayDF(*args, **kwargs):
    y = yesterday(*args, **kwargs)
    if y:
        df = _reindex(_toDatetime(json_normalize(y)), "symbol")
    else:
        df = pd.DataFrame()
    return df


previousDF = yesterdayDF


def price(symbol, token="", version="stable", filter="", format="json"):
    """Price of ticker

    https://iexcloud.io/docs/api/#price
    4:30am-8pm ET Mon-Fri

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
        "stock/{symbol}/price".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(price)
def priceDF(*args, **kwargs):
    return _toDatetime(json_normalize({"price": price(*args, **kwargs)}))


def quote(symbol, token="", version="stable", filter="", format="json"):
    """Get quote for ticker

    https://iexcloud.io/docs/api/#quote
    4:30am-8pm ET Mon-Fri


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
        "stock/{symbol}/quote".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(quote)
def quoteDF(*args, **kwargs):
    q = quote(*args, **kwargs)
    if q:
        df = _reindex(_toDatetime(json_normalize(q)), "symbol")
    else:
        df = pd.DataFrame()
    return df


@_expire(hour=8, tz=_EST)
def spread(symbol, token="", version="stable", filter="", format="json"):
    """This returns an array of effective spread, eligible volume, and price improvement of a stock, by market.
    Unlike volume-by-venue, this will only return a venue if effective spread is not ‘N/A’. Values are sorted in descending order by effectiveSpread.
    Lower effectiveSpread and higher priceImprovement values are generally considered optimal.

    Effective spread is designed to measure marketable orders executed in relation to the market center’s
    quoted spread and takes into account hidden and midpoint liquidity available at each market center.
    Effective Spread is calculated by using eligible trade prices recorded to the consolidated tape and
    comparing those trade prices to the National Best Bid and Offer (“NBBO”) at the time of the execution.

    View the data disclaimer at the bottom of the stocks app for more information about how these values are calculated.

    8am ET M-F

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
        "stock/{symbol}/effective-spread".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(spread)
def spreadDF(*args, **kwargs):
    return _reindex(_toDatetime(pd.DataFrame(spread(*args, **kwargs))), "venue")


def volumeByVenue(symbol, token="", version="stable", filter="", format="json"):
    """This returns 15 minute delayed and 30 day average consolidated volume percentage of a stock, by market.
    This call will always return 13 values, and will be sorted in ascending order by current day trading volume percentage.

    https://iexcloud.io/docs/api/#volume-by-venue
    Updated during regular market hours 9:30am-4pm ET


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
        "stock/{symbol}/volume-by-venue".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(volumeByVenue)
def volumeByVenueDF(*args, **kwargs):
    return _reindex(_toDatetime(pd.DataFrame(volumeByVenue(*args, **kwargs))), "venue")

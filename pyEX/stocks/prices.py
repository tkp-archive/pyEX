# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _expire, _TIMEFRAME_CHART, _getJson, _raiseIfNotStr, PyEXception, _strOrDate, _reindex, _toDatetime, _EST


def book(symbol, token='', version='', filter=''):
    '''Book data

    https://iextrading.com/developer/docs/#book
    realtime during Investors Exchange market hours

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/book', token, version, filter)


def _bookToDF(b):
    '''internal'''
    quote = b.get('quote', [])
    asks = b.get('asks', [])
    bids = b.get('bids', [])
    trades = b.get('trades', [])

    df1 = pd.io.json.json_normalize(quote)
    df1['type'] = 'quote'

    df2 = pd.io.json.json_normalize(asks)
    df2['symbol'] = quote['symbol']
    df2['type'] = 'ask'

    df3 = pd.io.json.json_normalize(bids)
    df3['symbol'] = quote['symbol']
    df3['type'] = 'bid'

    df4 = pd.io.json.json_normalize(trades)
    df4['symbol'] = quote['symbol']
    df3['type'] = 'trade'

    df = pd.concat([df1, df2, df3, df4], sort=True)
    _toDatetime(df)
    return df


def bookDF(symbol, token='', version='', filter=''):
    '''Book data

    https://iextrading.com/developer/docs/#book
    realtime during Investors Exchange market hours

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    x = book(symbol, token, version, filter)
    df = _bookToDF(x)
    return df


@_expire(hour=4, tz=_EST)
def chart(symbol, timeframe='1m', date=None, token='', version='', filter=''):
    '''Historical price/volume data, daily and intraday

    https://iexcloud.io/docs/api/#historical-prices
    Data Schedule
    1d: -9:30-4pm ET Mon-Fri on regular market trading days
        -9:30-1pm ET on early close trading days
    All others:
        -Prior trading day available after 4am ET Tue-Sat

    Args:
        symbol (string); Ticker to request
        timeframe (string); Timeframe to request e.g. 1m
        date (datetime): date, if requesting intraday
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if timeframe is not None and timeframe != '1d':
        if timeframe not in _TIMEFRAME_CHART:
            raise PyEXception('Range must be in %s' % str(_TIMEFRAME_CHART))
        return _getJson('stock/' + symbol + '/chart' + '/' + timeframe, token, version, filter)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/' + symbol + '/chart' + '/date/' + date, token, version, filter)
    return _getJson('stock/' + symbol + '/chart', token, version, filter)


def _chartToDF(c):
    '''internal'''
    df = pd.DataFrame(c)
    _toDatetime(df)
    _reindex(df, 'date')
    return df


@_expire(second=0)
def chartDF(symbol, timeframe='1m', date=None, token='', version='', filter=''):
    '''Historical price/volume data, daily and intraday

    https://iexcloud.io/docs/api/#historical-prices
    Data Schedule
    1d: -9:30-4pm ET Mon-Fri on regular market trading days
        -9:30-1pm ET on early close trading days
    All others:
        -Prior trading day available after 4am ET Tue-Sat

    Args:
        symbol (string); Ticker to request
        timeframe (string); Timeframe to request e.g. 1m
        date (datetime): date, if requesting intraday
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    c = chart(symbol, timeframe, date, token, version, filter)
    df = pd.DataFrame(c)
    _toDatetime(df)
    if timeframe is not None and timeframe != '1d':
        _reindex(df, 'date')
    else:
        if not df.empty:
            df.set_index(['date', 'minute'], inplace=True)
        else:
            return pd.DataFrame()
    return df


@_expire(second=0)
def delayedQuote(symbol, token='', version='', filter=''):
    '''This returns the 15 minute delayed market quote.

    https://iexcloud.io/docs/api/#delayed-quote
    15min delayed
    4:30am - 8pm ET M-F when market is open

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/delayed-quote', token, version, filter)


def delayedQuoteDF(symbol, token='', version='', filter=''):
    '''This returns the 15 minute delayed market quote.

    https://iexcloud.io/docs/api/#delayed-quote
    15min delayed
    4:30am - 8pm ET M-F when market is open

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(delayedQuote(symbol, token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def intraday(symbol, token='', version='', filter=''):
    '''This endpoint will return aggregated intraday prices in one minute buckets

    https://iexcloud.io/docs/api/#intraday-prices
    9:30-4pm ET Mon-Fri on regular market trading days
    9:30-1pm ET on early close trading days


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/intraday-prices', token, version, filter)


def intradayDF(symbol, token='', version='', filter=''):
    '''This endpoint will return aggregated intraday prices in one minute buckets

    https://iexcloud.io/docs/api/#intraday-prices
    9:30-4pm ET Mon-Fri on regular market trading days
    9:30-1pm ET on early close trading days


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    val = intraday(symbol, token, version, filter)
    df = pd.DataFrame(val)
    _toDatetime(df)
    _reindex(df, 'minute')
    return df


def largestTrades(symbol, token='', version='', filter=''):
    '''This returns 15 minute delayed, last sale eligible trades.

    https://iexcloud.io/docs/api/#largest-trades
    9:30-4pm ET M-F during regular market hours

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/largest-trades', token, version, filter)


def largestTradesDF(symbol, token='', version='', filter=''):
    '''This returns 15 minute delayed, last sale eligible trades.

    https://iexcloud.io/docs/api/#largest-trades
    9:30-4pm ET M-F during regular market hours

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(largestTrades(symbol, token, version, filter))
    _toDatetime(df)
    _reindex(df, 'time')
    return df


def ohlc(symbol, token='', version='', filter=''):
    '''Returns the official open and close for a give symbol.

    https://iexcloud.io/docs/api/#news
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/ohlc', token, version, filter)


def ohlcDF(symbol, token='', version='', filter=''):
    '''Returns the official open and close for a give symbol.

    https://iexcloud.io/docs/api/#news
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    o = ohlc(symbol, token, version, filter)
    if o:
        df = pd.io.json.json_normalize(o)
        _toDatetime(df)
    else:
        df = pd.DataFrame()
    return df


@_expire(hour=4, tz=_EST)
def yesterday(symbol, token='', version='', filter=''):
    '''This returns previous day adjusted price data for one or more stocks

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/previous', token, version, filter)


def yesterdayDF(symbol, token='', version='', filter=''):
    '''This returns previous day adjusted price data for one or more stocks

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    y = yesterday(symbol, token, version, filter)
    if y:
        df = pd.io.json.json_normalize(y)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def price(symbol, token='', version='', filter=''):
    '''Price of ticker

    https://iexcloud.io/docs/api/#price
    4:30am-8pm ET Mon-Fri

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/price', token, version, filter)


def priceDF(symbol, token='', version='', filter=''):
    '''Price of ticker

    https://iexcloud.io/docs/api/#price
    4:30am-8pm ET Mon-Fri

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize({'price': price(symbol, token, version, filter)})
    _toDatetime(df)
    return df


def quote(symbol, token='', version='', filter=''):
    '''Get quote for ticker

    https://iexcloud.io/docs/api/#quote
    4:30am-8pm ET Mon-Fri


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/quote', token, version, filter)


def quoteDF(symbol, token='', version='', filter=''):
    '''Get quote for ticker

    https://iexcloud.io/docs/api/#quote
    4:30am-8pm ET Mon-Fri


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    q = quote(symbol, token, version, filter)
    if q:
        df = pd.io.json.json_normalize(q)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


@_expire(hour=8, tz=_EST)
def spread(symbol, token='', version='', filter=''):
    '''This returns an array of effective spread, eligible volume, and price improvement of a stock, by market.
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
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/effective-spread', token, version, filter)


def spreadDF(symbol, token='', version='', filter=''):
    '''This returns an array of effective spread, eligible volume, and price improvement of a stock, by market.
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
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(spread(symbol, token, version, filter))
    _toDatetime(df)
    _reindex(df, 'venue')
    return df


def volumeByVenue(symbol, token='', version='', filter=''):
    '''This returns 15 minute delayed and 30 day average consolidated volume percentage of a stock, by market.
    This call will always return 13 values, and will be sorted in ascending order by current day trading volume percentage.

    https://iexcloud.io/docs/api/#volume-by-venue
    Updated during regular market hours 9:30am-4pm ET


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/volume-by-venue', token, version, filter)


def volumeByVenueDF(symbol, token='', version='', filter=''):
    '''This returns 15 minute delayed and 30 day average consolidated volume percentage of a stock, by market.
    This call will always return 13 values, and will be sorted in ascending order by current day trading volume percentage.

    https://iexcloud.io/docs/api/#volume-by-venue
    Updated during regular market hours 9:30am-4pm ET


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(volumeByVenue(symbol, token, version, filter))
    _toDatetime(df)
    _reindex(df, 'venue')
    return df

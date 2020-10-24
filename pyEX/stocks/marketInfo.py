# -*- coding: utf-8 -*-
from functools import wraps
import pandas as pd
from ..common import _expire, _LIST_OPTIONS, _COLLECTION_TAGS, _getJson, _raiseIfNotStr, PyEXception, _strOrDate, _reindex, _toDatetime, _UTC, _EST


@_expire(hour=0)
def collections(tag, collectionName, token='', version='', filter=''):
    '''Returns an array of quote objects for a given collection type. Currently supported collection types are sector, tag, and list


    https://iexcloud.io/docs/api/#collections

    Args:
        tag (str):  Sector, Tag, or List
        collectionName (str):  Associated name for tag
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    if tag not in _COLLECTION_TAGS:
        raise PyEXception('Tag must be in %s' % str(_COLLECTION_TAGS))
    return _getJson('stock/market/collection/' + tag + '?collectionName=' + collectionName, token, version, filter)


@wraps(collections)
def collectionsDF(tag, query, token='', version='', filter=''):
    df = pd.DataFrame(collections(tag, query, token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


@_expire(minute=0)
def earningsToday(token='', version='', filter=''):
    '''Returns earnings that will be reported today as two arrays: before the open bto and after market close amc.
    Each array contains an object with all keys from earnings, a quote object, and a headline key.

    https://iexcloud.io/docs/api/#earnings-today
    Updates at 9am, 11am, 12pm UTC daily


    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return _getJson('stock/market/today-earnings', token, version, filter)


@wraps(earningsToday)
def earningsTodayDF(token='', version='', filter=''):
    x = earningsToday(token, version, filter)
    z = []
    for k in x:
        ds = x[k]
        for d in ds:
            d['when'] = k
            z.extend(ds)
    df = pd.io.json.json_normalize(z)

    if not df.empty:
        df.drop_duplicates(inplace=True)

    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


@_expire(hour=10, tz=_UTC)
def ipoToday(token='', version='', filter=''):
    '''This returns a list of upcoming or today IPOs scheduled for the current and next month. The response is split into two structures:
    rawData and viewData. rawData represents all available data for an IPO. viewData represents data structured for display to a user.

    https://iexcloud.io/docs/api/#ipo-calendar
    10am, 10:30am UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return _getJson('stock/market/today-ipos', token, version, filter)


@wraps(ipoToday)
def ipoTodayDF(token='', version='', filter=''):
    val = ipoToday(token, version, filter)
    if val:
        df = pd.io.json.json_normalize(val, 'rawData')
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


@_expire(hour=10)
def ipoUpcoming(token='', version='', filter=''):
    '''This returns a list of upcoming or today IPOs scheduled for the current and next month. The response is split into two structures:
    rawData and viewData. rawData represents all available data for an IPO. viewData represents data structured for display to a user.

    https://iexcloud.io/docs/api/#ipo-calendar
    10am, 10:30am UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return _getJson('stock/market/upcoming-ipos', token, version, filter)


@wraps(ipoUpcoming)
def ipoUpcomingDF(token='', version='', filter=''):
    val = ipoUpcoming(token, version, filter)
    if val:
        df = pd.io.json.json_normalize(val, 'rawData')
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def list(option='mostactive', token='', version='', filter=''):
    '''Returns an array of quotes for the top 10 symbols in a specified list.


    https://iexcloud.io/docs/api/#list
    Updated intraday

    Args:
        option (str): Option to query
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    if option not in _LIST_OPTIONS:
        raise PyEXception('Option must be in %s' % str(_LIST_OPTIONS))
    return _getJson('stock/market/list/' + option, token, version, filter)


@wraps(list)
def listDF(option='mostactive', token='', version='', filter=''):
    df = pd.DataFrame(list(option, token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def marketVolume(token='', version='', filter=''):
    '''This endpoint returns real time traded volume on U.S. markets.

    https://iexcloud.io/docs/api/#market-volume-u-s
    7:45am-5:15pm ET Mon-Fri

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return _getJson('market/', token, version, filter)


@wraps(marketVolume)
def marketVolumeDF(token='', version='', filter=''):
    df = pd.DataFrame(marketVolume())
    _toDatetime(df, cols=[], tcols=['lastUpdated'])
    return df


def marketOhlc(token='', version='', filter=''):
    '''Returns the official open and close for whole market.

    https://iexcloud.io/docs/api/#news
    9:30am-5pm ET Mon-Fri

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return _getJson('stock/market/ohlc', token, version, filter)


@wraps(marketOhlc)
def marketOhlcDF(token='', version='', filter=''):
    x = marketOhlc(token, version, filter)
    data = []
    for key in x:
        data.append(x[key])
        data[-1]['symbol'] = key
    df = pd.io.json.json_normalize(data)
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


@_expire(hour=4, tz=_UTC)
def marketYesterday(token='', version='', filter=''):
    '''This returns previous day adjusted price data for whole market

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return _getJson('stock/market/previous', token, version, filter)


@wraps(marketYesterday)
def marketYesterdayDF(token='', version='', filter=''):
    x = marketYesterday(token, version, filter)
    data = []
    for key in x:
        data.append(x[key])
        data[-1]['symbol'] = key
    df = pd.DataFrame(data)
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def sectorPerformance(token='', version='', filter=''):
    '''This returns an array of each sector and performance for the current trading day. Performance is based on each sector ETF.

    https://iexcloud.io/docs/api/#sector-performance
    8am-5pm ET Mon-Fri

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return _getJson('stock/market/sector-performance', token, version, filter)


@wraps(sectorPerformance)
def sectorPerformanceDF(token='', version='', filter=''):
    df = pd.DataFrame(sectorPerformance(token, version, filter))
    _toDatetime(df, cols=[], tcols=['lastUpdated'])
    _reindex(df, 'name')
    return df


@_expire(hour=16, tz=_EST)
def marketShortInterest(date=None, token='', version='', filter=''):
    '''The consolidated market short interest positions in all IEX-listed securities are included in the IEX Short Interest Report.

    The report data will be published daily at 4:00pm ET.

    https://iexcloud.io/docs/api/#listed-short-interest-list-in-dev

    Args:
        date (datetime): Effective Datetime
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('stock/market/short-interest/' + date, token, version, filter)
    return _getJson('stock/market/short-interest', token, version, filter)


@wraps(marketShortInterest)
def marketShortInterestDF(date=None, token='', version='', filter=''):
    df = pd.DataFrame(marketShortInterest(date, token, version, filter))
    _toDatetime(df)
    return df


def upcomingEvents(symbol='', refid='', token='', version='', filter=''):
    '''This will return all upcoming estimates, dividends, splits for a given symbol or the market. If market is passed for the symbol, IPOs will also be included.

    https://iexcloud.io/docs/api/#upcoming-events

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result

    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('stock/' + symbol + '/upcoming-events', token, version, filter)
    return _getJson('stock/market/upcoming-events', token, version, filter)


@wraps(upcomingEvents)
def upcomingEventsDF(symbol='', token='', version='', filter=''):
    return pd.io.json.json_normalize(upcomingEvents(symbol=symbol, token=token, version=version, filter=filter))


def upcomingEarnings(symbol='', refid='', token='', version='', filter=''):
    '''This will return all upcoming estimates, dividends, splits for a given symbol or the market. If market is passed for the symbol, IPOs will also be included.

    https://iexcloud.io/docs/api/#upcoming-events

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result

    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('stock/' + symbol + '/upcoming-earnings', token, version, filter)
    return _getJson('stock/market/upcoming-earnings', token, version, filter)


@wraps(upcomingEarnings)
def upcomingEarningsDF(symbol='', token='', version='', filter=''):
    return pd.io.json.json_normalize(upcomingEarnings(symbol=symbol, token=token, version=version, filter=filter))


def upcomingDividends(symbol='', refid='', token='', version='', filter=''):
    '''This will return all upcoming estimates, dividends, splits for a given symbol or the market. If market is passed for the symbol, IPOs will also be included.

    https://iexcloud.io/docs/api/#upcoming-events

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result

    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('stock/' + symbol + '/upcoming-dividends', token, version, filter)
    return _getJson('stock/market/upcoming-dividends', token, version, filter)


@wraps(upcomingDividends)
def upcomingDividendsDF(symbol='', token='', version='', filter=''):
    return pd.io.json.json_normalize(upcomingDividends(symbol=symbol, token=token, version=version, filter=filter))


def upcomingSplits(symbol='', refid='', token='', version='', filter=''):
    '''This will return all upcoming estimates, dividends, splits for a given symbol or the market. If market is passed for the symbol, IPOs will also be included.

    https://iexcloud.io/docs/api/#upcoming-events

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result

    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('stock/' + symbol + '/upcoming-splits', token, version, filter)
    return _getJson('stock/market/upcoming-splits', token, version, filter)


@wraps(upcomingSplits)
def upcomingSplitsDF(symbol='', token='', version='', filter=''):
    return pd.io.json.json_normalize(upcomingSplits(symbol=symbol, token=token, version=version, filter=filter))


def upcomingIPOs(symbol='', refid='', token='', version='', filter=''):
    '''This will return all upcoming estimates, dividends, splits for a given symbol or the market. If market is passed for the symbol, IPOs will also be included.

    https://iexcloud.io/docs/api/#upcoming-events

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result

    '''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('stock/' + symbol + '/upcoming-ipos', token, version, filter)
    return _getJson('stock/market/upcoming-ipos', token, version, filter)


@wraps(upcomingIPOs)
def upcomingIPOsDF(symbol='', token='', version='', filter=''):
    return pd.io.json.json_normalize(upcomingIPOs(symbol=symbol, token=token, version=version, filter=filter))

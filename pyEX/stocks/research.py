# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _expire, _getJson, _raiseIfNotStr, _reindex, _toDatetime, _EST, _UTC


@_expire(hour=4, tz=_EST)
def advancedStats(symbol, token='', version='', filter=''):
    '''Returns everything in key stats plus additional advanced stats such as EBITDA, ratios, key financial data, and more.

    https://iexcloud.io/docs/api/#advanced-stats
    4am, 5am ET

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/advanced-stats', token, version, filter)


def advancedStatsDF(symbol, token='', version='', filter=''):
    '''Returns everything in key stats plus additional advanced stats such as EBITDA, ratios, key financial data, and more.

    https://iexcloud.io/docs/api/#advanced-stats
    4am, 5am ET

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    val = advancedStats(symbol, token, version, filter)
    df = pd.io.json.json_normalize(val)
    _toDatetime(df)
    return df


@_expire(hour=9, tz=_UTC)
def analystRecommendations(symbol, token='', version='', filter=''):
    '''Pulls data from the last four months.

    https://iexcloud.io/docs/api/#analyst-recommendations
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/recommendation-trends', token, version, filter)


def analystRecommendationsDF(symbol, token='', version='', filter=''):
    '''Pulls data from the last four months.

    https://iexcloud.io/docs/api/#analyst-recommendations
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    val = analystRecommendations(symbol, token, version, filter)
    df = pd.io.json.json_normalize(val)
    _toDatetime(df)
    return df


def estimates(symbol, token='', version='', filter=''):
    '''Provides the latest consensus estimate for the next fiscal period

    https://iexcloud.io/docs/api/#estimates
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/estimates', token, version, filter)


def _estimatesToDF(f):
    '''internal'''
    if f:
        df = pd.io.json.json_normalize(f, 'estimates', 'symbol')
        _toDatetime(df)
        _reindex(df, 'fiscalEndDate')
    else:
        df = pd.DataFrame()
    return df


def estimatesDF(symbol, token='', version='', filter=''):
    '''Provides the latest consensus estimate for the next fiscal period

    https://iexcloud.io/docs/api/#estimates
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    f = estimates(symbol, token, version, filter)
    df = _estimatesToDF(f)
    return df


@_expire(hour=5, tz=_EST)
def fundOwnership(symbol, token='', version='', filter=''):
    '''Returns the top 10 fund holders, meaning any firm not defined as buy-side or sell-side such as mutual funds,
       pension funds, endowments, investment firms, and other large entities that manage funds on behalf of others.

    https://iexcloud.io/docs/api/#fund-ownership
    Updates at 5am, 6am ET every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/fund-ownership', token, version, filter)


def fundOwnershipDF(symbol, token='', version='', filter=''):
    '''Returns the top 10 fund holders, meaning any firm not defined as buy-side or sell-side such as mutual funds,
       pension funds, endowments, investment firms, and other large entities that manage funds on behalf of others.

    https://iexcloud.io/docs/api/#fund-ownership
    Updates at 5am, 6am ET every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:

        DataFrame: result
    '''
    val = fundOwnership(symbol, token, version, filter)
    df = pd.DataFrame(val)
    _toDatetime(df)
    return df


@_expire(hour=5, tz=_EST)
def institutionalOwnership(symbol, token='', version='', filter=''):
    '''Returns the top 10 institutional holders, defined as buy-side or sell-side firms.

    https://iexcloud.io/docs/api/#institutional-ownership
    Updates at 5am, 6am ET every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/institutional-ownership', token, version, filter)


def institutionalOwnershipDF(symbol, token='', version='', filter=''):
    '''Returns the top 10 institutional holders, defined as buy-side or sell-side firms.

    https://iexcloud.io/docs/api/#institutional-ownership
    Updates at 5am, 6am ET every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    val = institutionalOwnership(symbol, token, version, filter)
    df = pd.DataFrame(val)
    _toDatetime(df, cols=[], tcols=['reportDate'])
    return df


@_expire(hour=8, tz=_EST)
def keyStats(symbol, token='', version='', filter=''):
    '''Key Stats about company

    https://iexcloud.io/docs/api/#key-stats
    8am, 9am ET

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/stats', token, version, filter)


def _statsToDF(s):
    '''internal'''
    if s:
        df = pd.io.json.json_normalize(s)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def keyStatsDF(symbol, token='', version='', filter=''):
    '''Key Stats about company

    https://iexcloud.io/docs/api/#key-stats
    8am, 9am ET

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    s = keyStats(symbol, token, version, filter)
    df = _statsToDF(s)
    return df


def priceTarget(symbol, token='', version='', filter=''):
    '''Provides the latest avg, high, and low analyst price target for a symbol.

    https://iexcloud.io/docs/api/#price-target
    Updates at 10am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/price-target', token, version, filter)


def priceTargetDF(symbol, token='', version='', filter=''):
    '''Provides the latest avg, high, and low analyst price target for a symbol.

    https://iexcloud.io/docs/api/#price-target
    Updates at 10am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(priceTarget(symbol, token, version, filter))
    _toDatetime(df)
    return df


# TODO
# https://iexcloud.io/docs/api/#technical-indicators

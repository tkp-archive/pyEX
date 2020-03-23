# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from ..common import _expire, _TIMEFRAME_DIVSPLIT, _getJson, _raiseIfNotStr, PyEXception, _reindex, _toDatetime, _UTC


@_expire(hour=8, tz=_UTC)
def balanceSheet(symbol, token='', version='', filter=''):
    '''Pulls balance sheet data. Available quarterly (4 quarters) and annually (4 years)

    https://iexcloud.io/docs/api/#balance-sheet
    Updates at 8am, 9am UTC daily


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/balance-sheet', token, version, filter)


def balanceSheetDF(symbol, token='', version='', filter=''):
    '''Pulls balance sheet data. Available quarterly (4 quarters) and annually (4 years)

    https://iexcloud.io/docs/api/#balance-sheet
    Updates at 8am, 9am UTC daily


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    val = balanceSheet(symbol, token, version, filter)
    df = pd.io.json.json_normalize(val, 'balancesheet', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    return df


@_expire(hour=8, tz=_UTC)
def cashFlow(symbol, token='', version='', filter=''):
    '''Pulls cash flow data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#cash-flow
    Updates at 8am, 9am UTC daily


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/cash-flow', token, version, filter)


def cashFlowDF(symbol, token='', version='', filter=''):
    '''Pulls cash flow data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#cash-flow
    Updates at 8am, 9am UTC daily


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    val = cashFlow(symbol, token, version, filter)
    df = pd.io.json.json_normalize(val, 'cashflow', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    df.replace(to_replace=[None], value=np.nan, inplace=True)
    return df


@_expire(hour=9, tz=_UTC)
def dividends(symbol, timeframe='ytd', token='', version='', filter=''):
    '''Dividend history

    https://iexcloud.io/docs/api/#dividends
    Updated at 9am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/dividends/' + timeframe, token, version, filter)


def _dividendsToDF(d):
    '''internal'''
    df = pd.DataFrame(d)
    _toDatetime(df)
    _reindex(df, 'exDate')
    return df


def dividendsDF(symbol, timeframe='ytd', token='', version='', filter=''):
    '''Dividend history

    https://iexcloud.io/docs/api/#dividends
    Updated at 9am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    d = dividends(symbol, timeframe, token, version, filter)
    df = _dividendsToDF(d)
    return df


@_expire(hour=9, tz=_UTC)
def earnings(symbol, token='', version='', filter=''):
    '''Earnings data for a given company including the actual EPS, consensus, and fiscal period. Earnings are available quarterly (last 4 quarters) and annually (last 4 years).

    https://iexcloud.io/docs/api/#earnings
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
    return _getJson('stock/' + symbol + '/earnings', token, version, filter)


def _earningsToDF(e):
    '''internal'''
    if e:
        df = pd.io.json.json_normalize(e, 'earnings', 'symbol')
        _toDatetime(df)
        _reindex(df, 'EPSReportDate')
    else:
        df = pd.DataFrame()
    return df


def earningsDF(symbol, token='', version='', filter=''):
    '''Earnings data for a given company including the actual EPS, consensus, and fiscal period. Earnings are available quarterly (last 4 quarters) and annually (last 4 years).

    https://iexcloud.io/docs/api/#earnings
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    e = earnings(symbol, token, version, filter)
    df = _earningsToDF(e)
    return df


@_expire(hour=8, tz=_UTC)
def financials(symbol, token='', version='', filter=''):
    '''Pulls income statement, balance sheet, and cash flow data from the four most recent reported quarters.

    https://iexcloud.io/docs/api/#financials
    Updates at 8am, 9am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/financials', token, version, filter)


def _financialsToDF(f):
    '''internal'''
    if f:
        df = pd.io.json.json_normalize(f, 'financials', 'symbol')
        _toDatetime(df)
        _reindex(df, 'reportDate')
    else:
        df = pd.DataFrame()
    return df


def financialsDF(symbol, token='', version='', filter=''):
    '''Pulls income statement, balance sheet, and cash flow data from the four most recent reported quarters.

    https://iexcloud.io/docs/api/#financials
    Updates at 8am, 9am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    f = financials(symbol, token, version, filter)
    df = _financialsToDF(f)
    return df


@_expire(hour=8, tz=_UTC)
def incomeStatement(symbol, token='', version='', filter=''):
    '''Pulls income statement data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#income-statement
    Updates at 8am, 9am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/income', token, version, filter)


def incomeStatementDF(symbol, token='', version='', filter=''):
    '''Pulls income statement data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#income-statement
    Updates at 8am, 9am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    val = incomeStatement(symbol, token, version, filter)
    df = pd.io.json.json_normalize(val, 'income', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    return df


@_expire(hour=9, tz=_UTC)
def stockSplits(symbol, timeframe='ytd', token='', version='', filter=''):
    '''Stock split history

    https://iexcloud.io/docs/api/#splits
    Updated at 9am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/splits/' + timeframe, token, version, filter)


def _splitsToDF(s):
    '''internal'''
    df = pd.DataFrame(s)
    _toDatetime(df)
    _reindex(df, 'exDate')
    return df


def stockSplitsDF(symbol, timeframe='ytd', token='', version='', filter=''):
    '''Stock split history

    https://iexcloud.io/docs/api/#splits
    Updated at 9am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    s = stockSplits(symbol, timeframe, token, version, filter)
    df = _splitsToDF(s)
    return df

# -*- coding: utf-8 -*-
from functools import wraps
import pandas as pd
import numpy as np
from ..common import _expire, _TIMEFRAME_DIVSPLIT, _getJson, _raiseIfNotStr, PyEXception, _reindex, _toDatetime, _checkPeriodLast, _UTC


@_expire(hour=8, tz=_UTC)
def balanceSheet(symbol, period='quarter', last=1, token='', version='', filter=''):
    '''Pulls balance sheet data. Available quarterly (4 quarters) and annually (4 years)

    https://iexcloud.io/docs/api/#balance-sheet
    Updates at 8am, 9am UTC daily


    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    _checkPeriodLast(period, last)
    return _getJson('stock/{}/balance-sheet?period={}&last={}'.format(symbol, period, last), token, version, filter)


@wraps(balanceSheet)
def balanceSheetDF(symbol, period='quarter', last=1, token='', version='', filter=''):
    val = balanceSheet(symbol, period, last, token, version, filter)
    df = pd.io.json.json_normalize(val, 'balancesheet', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    return df


@_expire(hour=8, tz=_UTC)
def cashFlow(symbol, period='quarter', last=1, token='', version='', filter=''):
    '''Pulls cash flow data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#cash-flow
    Updates at 8am, 9am UTC daily


    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    _checkPeriodLast(period, last)
    return _getJson('stock/{}/cash-flow?period={}&last={}'.format(symbol, period, last), token, version, filter)


@wraps(cashFlow)
def cashFlowDF(symbol, period='quarter', last=1, token='', version='', filter=''):
    val = cashFlow(symbol, period, last, token, version, filter)
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
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
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


@wraps(dividends)
def dividendsDF(symbol, timeframe='ytd', token='', version='', filter=''):
    d = dividends(symbol, timeframe, token, version, filter)
    df = _dividendsToDF(d)
    return df


@_expire(hour=9, tz=_UTC)
def earnings(symbol, period='quarter', last=1, field='', token='', version='', filter=''):
    '''Earnings data for a given company including the actual EPS, consensus, and fiscal period. Earnings are available quarterly (last 4 quarters) and annually (last 4 years).

    https://iexcloud.io/docs/api/#earnings
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    _checkPeriodLast(period, last)
    if not field:
        return _getJson('stock/{}/earnings?period={}&last={}'.format(symbol, period, last), token, version, filter)
    return _getJson('stock/{}/earnings/{}/{}?period={}'.format(symbol, last, field, period), token, version, filter)


def _earningsToDF(e):
    '''internal'''
    if e:
        df = pd.io.json.json_normalize(e, 'earnings', 'symbol')
        _toDatetime(df)
        _reindex(df, 'EPSReportDate')
    else:
        df = pd.DataFrame()
    return df


@wraps(earnings)
def earningsDF(symbol, period='quarter', last=1, field='', token='', version='', filter=''):
    e = earnings(symbol, period, last, field, token, version, filter)
    df = _earningsToDF(e)
    return df


@_expire(hour=8, tz=_UTC)
def financials(symbol, period='quarter', token='', version='', filter=''):
    '''Pulls income statement, balance sheet, and cash flow data from the four most recent reported quarters.

    https://iexcloud.io/docs/api/#financials
    Updates at 8am, 9am UTC daily

    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    _checkPeriodLast(period, 1)
    return _getJson('stock/{}/financials?period={}'.format(symbol, period), token, version, filter)


def _financialsToDF(f):
    '''internal'''
    if f:
        df = pd.io.json.json_normalize(f, 'financials', 'symbol')
        _toDatetime(df)
        _reindex(df, 'reportDate')
    else:
        df = pd.DataFrame()
    return df


@wraps(financials)
def financialsDF(symbol, period='quarter', token='', version='', filter=''):
    f = financials(symbol, period, token, version, filter)
    df = _financialsToDF(f)
    return df


@_expire(hour=8, tz=_UTC)
def incomeStatement(symbol, period='quarter', last=1, token='', version='', filter=''):
    '''Pulls income statement data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#income-statement
    Updates at 8am, 9am UTC daily

    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    _checkPeriodLast(period, last)
    return _getJson('stock/{}/income?period={}&last={}'.format(symbol, period, last), token, version, filter)


@wraps(incomeStatement)
def incomeStatementDF(symbol, period='quarter', last=1, token='', version='', filter=''):
    val = incomeStatement(symbol, period, last, token, version, filter)
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
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
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


@wraps(stockSplits)
def stockSplitsDF(symbol, timeframe='ytd', token='', version='', filter=''):
    s = stockSplits(symbol, timeframe, token, version, filter)
    df = _splitsToDF(s)
    return df

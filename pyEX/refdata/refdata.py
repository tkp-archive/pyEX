# -*- coding: utf-8 -*-
import pandas as pd
from deprecation import deprecated
from functools import wraps
from ..common import _getJson, _strOrDate, _toDatetime


@deprecated(details='Deprecated: IEX Cloud status unkown')
def corporateActions(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/corporate-actions/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/corporate-actions', token, version, filter)


@wraps(corporateActions)
@deprecated(details='Deprecated: IEX Cloud status unkown')
def corporateActionsDF(date=None, token='', version='', filter=''):
    df = pd.DataFrame(corporateActions(date, token, version, filter))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def dividends(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/dividends/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/dividends', token, version, filter)


@wraps(dividends)
@deprecated(details='Deprecated: IEX Cloud status unkown')
def dividendsDF(date=None, token='', version='', filter=''):
    df = pd.DataFrame(dividends(date, token, version, filter))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def nextDayExtDate(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/next-day-ex-date/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/next-day-ex-date', token, version, filter)


@wraps(nextDayExtDate)
@deprecated(details='Deprecated: IEX Cloud status unkown')
def nextDayExtDateDF(date=None, token='', version='', filter=''):
    df = pd.DataFrame(nextDayExtDate(date, token, version, filter))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def directory(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/symbol-directory/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/symbol-directory', token, version, filter)


@wraps(directory)
@deprecated(details='Deprecated: IEX Cloud status unkown')
def directoryDF(date=None, token='', version='', filter=''):
    df = pd.DataFrame(directory(date, token, version, filter))
    _toDatetime(df)
    return df

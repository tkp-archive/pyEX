# -*- coding: utf-8 -*-
import pandas as pd
from deprecation import deprecated
from ..common import _getJson, _strOrDate, _toDatetime


@deprecated(details='Deprecated: IEX Cloud status unkown')
def corporateActions(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/corporate-actions/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/corporate-actions', token, version, filter)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def corporateActionsDF(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(corporateActions(date, token, version, filter))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def dividends(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/dividends/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/dividends', token, version, filter)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def dividendsDF(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(dividends(date, token, version, filter))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def nextDayExtDate(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/next-day-ex-date/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/next-day-ex-date', token, version, filter)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def nextDayExtDateDF(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(nextDayExtDate(date, token, version, filter))
    _toDatetime(df)
    return df


@deprecated(details='Deprecated: IEX Cloud status unkown')
def directory(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/symbol-directory/' + date, token, version, filter)
    return _getJson('ref-data/daily-list/symbol-directory', token, version, filter)


@deprecated(details='Deprecated: IEX Cloud status unkown')
def directoryDF(date=None, token='', version='', filter=''):
    '''

    Args:
        date (datetime): Effective date
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    df = pd.DataFrame(directory(date, token, version, filter))
    _toDatetime(df)
    return df

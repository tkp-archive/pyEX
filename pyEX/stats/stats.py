# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime
from ..common import _expire, _getJson, PyEXception, _strOrDate, _reindex, _toDatetime


def stats(token='', version='', filter=''):
    '''https://iexcloud.io/docs/api/#stats-intraday

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('stats/intraday', token, version, filter)


def statsDF(token='', version='', filters=''):
    '''https://iexcloud.io/docs/api/#stats-intraday

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(stats(token, version, filter))
    _toDatetime(df)
    return df


def recent(token='', version='', filter=''):
    '''https://iexcloud.io/docs/api/#stats-recent

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('stats/recent', token, version, filter)


def recentDF(token='', version='', filter=''):
    '''https://iexcloud.io/docs/api/#stats-recent

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(recent(token, version, filter))
    _toDatetime(df)
    _reindex(df, 'date')
    return df


def records(token='', version='', filter=''):
    '''https://iexcloud.io/docs/api/#stats-records

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('stats/records', token, version, filter)


def recordsDF(token='', version='', filter=''):
    '''https://iexcloud.io/docs/api/#stats-records

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(records(token, version, filter))
    _toDatetime(df)
    return df


@_expire(hour=0)
def summary(date=None, token='', version='', filter=''):
    '''https://iexcloud.io/docs/api/#stats-historical-summary

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        if isinstance(date, str):
            return _getJson('stats/historical?date=' + date, token, version, filter)
        elif isinstance(date, datetime):
            return _getJson('stats/historical?date=' + date.strftime('%Y%m'), token, version, filter)
        else:
            raise PyEXception("Can't handle type : %s" % str(type(date)), token, version, filter)
    return _getJson('stats/historical', token, version, filter)


def summaryDF(date=None, token='', version='', filter=''):
    '''https://iexcloud.io/docs/api/#stats-historical-summary

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(summary(date, token, version, filter))
    _toDatetime(df)
    return df


@_expire(hour=0)
def daily(date=None, last='', token='', version='', filter=''):
    '''https://iexcloud.io/docs/api/#stats-historical-daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('stats/historical/daily?date=' + date, token, version, filter)
    elif last:
        return _getJson('stats/historical/daily?last=' + last, token, version, filter)
    return _getJson('stats/historical/daily', token, version, filter)


def dailyDF(date=None, last='', token='', version='', filter=''):
    '''https://iexcloud.io/docs/api/#stats-historical-daily

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(daily(date, last, token, version, filter))
    _toDatetime(df)
    return df

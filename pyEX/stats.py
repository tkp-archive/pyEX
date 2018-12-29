import pandas as pd
from datetime import datetime
from .common import _getJson, PyEXception, _strOrDate, _reindex, _toDatetime


def stats(token='', version=''):
    '''https://iextrading.com/developer/docs/#intraday'''
    return _getJson('stats/intraday', token, version)


def statsDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#intraday'''
    df = pd.DataFrame(stats(token, version))
    _toDatetime(df)
    return df


def recent(token='', version=''):
    '''https://iextrading.com/developer/docs/#recent'''
    return _getJson('stats/recent', token, version)


def recentDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#recent'''
    df = pd.DataFrame(recent(token, version))
    _toDatetime(df)
    _reindex(df, 'date')
    return df


def records(token='', version=''):
    '''https://iextrading.com/developer/docs/#records'''
    return _getJson('stats/records', token, version)


def recordsDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#records'''
    df = pd.DataFrame(records(token, version))
    _toDatetime(df)
    return df


def summary(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#historical-summary'''
    if date:
        if isinstance(date, str):
            return _getJson('stats/historical?date=' + date, token, version)
        elif isinstance(date, datetime):
            return _getJson('stats/historical?date=' + date.strftime('%Y%m'), token, version)
        else:
            raise PyEXception("Can't handle type : %s" % str(type(date)), token, version)
    return _getJson('stats/historical', token, version)


def summaryDF(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#historical-summary'''
    df = pd.DataFrame(summary(date, token, version))
    _toDatetime(df)
    return df


def daily(date=None, last='', token='', version=''):
    '''https://iextrading.com/developer/docs/#historical-daily'''
    '''https://iextrading.com/developer/docs/#historical-summary'''
    if date:
        date = _strOrDate(date)
        return _getJson('stats/historical/daily?date=' + date, token, version)
    elif last:
        return _getJson('stats/historical/daily?last=' + last, token, version)
    return _getJson('stats/historical/daily', token, version)


def dailyDF(date=None, last='', token='', version=''):
    '''https://iextrading.com/developer/docs/#historical-daily'''
    '''https://iextrading.com/developer/docs/#historical-summary'''
    df = pd.DataFrame(daily(date, last, token, version))
    _toDatetime(df)
    return df

import pandas as pd
from datetime import datetime
from .common import _getJson, PyEXception, _strOrDate


def stats():
    '''https://iextrading.com/developer/docs/#intraday'''
    return _getJson('stats/intraday')


def statsDF():
    '''https://iextrading.com/developer/docs/#intraday'''
    return pd.DataFrame(stats())


def recent():
    '''https://iextrading.com/developer/docs/#recent'''
    return _getJson('stats/recent')


def recentDF():
    '''https://iextrading.com/developer/docs/#recent'''
    return pd.DataFrame(recent())


def records():
    '''https://iextrading.com/developer/docs/#records'''
    return _getJson('stats/records')


def recordsDF():
    '''https://iextrading.com/developer/docs/#records'''
    return pd.DataFrame(records())


def summary(date=None):
    '''https://iextrading.com/developer/docs/#historical-summary'''
    if date:
        if isinstance(date, str):
            return _getJson('stats/historical?date=' + date)
        elif isinstance(date, datetime):
            return _getJson('stats/historical?date=' + date.strftime('%Y%m'))
        else:
            raise PyEXception("Can't handle type : %s" % str(type(date)))
    return _getJson('stats/historical')


def summaryDF(date=None):
    '''https://iextrading.com/developer/docs/#historical-summary'''
    return pd.DataFrame(summary(date))


def daily(date=None, last=''):
    '''https://iextrading.com/developer/docs/#historical-daily'''
    '''https://iextrading.com/developer/docs/#historical-summary'''
    if date:
        date = _strOrDate(date)
        return _getJson('stats/historical/daily?date=' + date)
    elif last:
        return _getJson('stats/historical/daily?last=' + last)
    return _getJson('stats/historical/daily')


def dailyDF(date=None, last=''):
    '''https://iextrading.com/developer/docs/#historical-daily'''
    '''https://iextrading.com/developer/docs/#historical-summary'''
    return pd.DataFrame(daily(date, last))

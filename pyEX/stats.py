from datetime import datetime
from .common import _URL_PREFIX, _TIMEFRAME_CHART, _TIMEFRAME_DIVSPLIT, _LIST_OPTIONS, _getJson, _df


def stats():
    '''https://iextrading.com/developer/docs/#intraday'''
    return _getJson('stats/intraday')


def recent():
    '''https://iextrading.com/developer/docs/#recent'''
    return _getJson('stats/recent')


def records():
    '''https://iextrading.com/developer/docs/#records'''
    return _getJson('stats/records')


def summary(date=None):
    '''https://iextrading.com/developer/docs/#historical-summary'''
    if date:
        if isinstance(date, str):
            return _getJson('stats/historical?date=' + date)
        elif isinstance(date, datetime):
            return _getJson('stats/historical?date=' + date.strftime('%Y%m'))
        else:
            raise Exception("Can't handle type : %s" % str(type(date)))
    return _getJson('stats/historical')


def daily(date=None, last=''):
    '''https://iextrading.com/developer/docs/#historical-daily'''
    '''https://iextrading.com/developer/docs/#historical-summary'''
    if date:
        if isinstance(date, str):
            return _getJson('stats/historical/daily?date=' + date)
        elif isinstance(date, datetime):
            return _getJson('stats/historical/daily?date=' + date.strftime('%Y%m%d'))
        else:
            raise Exception("Can't handle type : %s" % str(type(date)))
    elif last:
        return _getJson('stats/historical/daily?last=' + last)
    return _getJson('stats/historical/daily')

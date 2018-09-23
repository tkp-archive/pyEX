import pandas as pd
from .common import _getJson, _strOrDate, _reindex, _toDatetime


def symbols():
    '''https://iextrading.com/developer/docs/#symbols'''
    return _getJson('ref-data/symbols')


def symbolsDF():
    '''https://iextrading.com/developer/docs/#symbols'''
    df = pd.DataFrame(symbols())
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def corporateActions(date=None):
    '''https://iextrading.com/developer/docs/#iex-corporate-actions'''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/corporate-actions/' + date)
    return _getJson('ref-data/daily-list/corporate-actions')


def corporateActionsDF(date=None):
    '''https://iextrading.com/developer/docs/#iex-corporate-actions'''
    df = pd.DataFrame(corporateActions(date))
    _toDatetime(df)
    return df


def dividends(date=None):
    '''https://iextrading.com/developer/docs/#iex-dividends'''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/dividends/' + date)
    return _getJson('ref-data/daily-list/dividends')


def dividendsDF(date=None):
    '''https://iextrading.com/developer/docs/#iex-dividends'''
    df = pd.DataFrame(dividends(date))
    _toDatetime(df)
    return df


def nextDayExtDate(date=None):
    '''https://iextrading.com/developer/docs/#iex-next-day-ex-date'''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/next-day-ex-date/' + date)
    return _getJson('ref-data/daily-list/next-day-ex-date')


def nextDayExtDateDF(date=None):
    '''https://iextrading.com/developer/docs/#iex-next-day-ex-date'''
    df = pd.DataFrame(nextDayExtDate(date))
    _toDatetime(df)
    return df


def directory(date=None):
    '''https://iextrading.com/developer/docs/#iex-listed-symbol-directory'''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/symbol-directory/' + date)
    return _getJson('ref-data/daily-list/symbol-directory')


def directoryDF(date=None):
    '''https://iextrading.com/developer/docs/#iex-listed-symbol-directory'''
    df = pd.DataFrame(directory(date))
    _toDatetime(df)
    return df

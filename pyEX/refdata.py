import pandas as pd
from .common import _getJson, _strOrDate, _reindex, _toDatetime


def symbols(token='', version=''):
    '''https://iextrading.com/developer/docs/#symbols'''
    return _getJson('ref-data/symbols', token, version)


def iexSymbols(token='', version=''):
    '''https://iexcloud.io/docs/api/#iex-symbols'''
    return _getJson('ref-data/iex/symbols', token, version)


def symbolsDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#symbols'''
    df = pd.DataFrame(symbols(token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def iexSymbolsDF(token='', version=''):
    '''https://iexcloud.io/docs/api/#iex-symbols'''
    df = pd.DataFrame(iexSymbols(token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def symbolsList(token='', version=''):
    '''https://iextrading.com/developer/docs/#symbols'''
    return symbolsDF(token, version).index.tolist()


def iexSymbolsList(token='', version=''):
    '''https://iexcloud.io/docs/api/#iex-symbols'''
    return iexSymbolsDF(token, version).index.tolist()


def corporateActions(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-corporate-actions'''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/corporate-actions/' + date, token, version)
    return _getJson('ref-data/daily-list/corporate-actions', token, version)


def corporateActionsDF(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-corporate-actions'''
    df = pd.DataFrame(corporateActions(date, token, version))
    _toDatetime(df)
    return df


def dividends(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-dividends'''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/dividends/' + date, token, version)
    return _getJson('ref-data/daily-list/dividends', token, version)


def dividendsDF(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-dividends'''
    df = pd.DataFrame(dividends(date, token, version))
    _toDatetime(df)
    return df


def nextDayExtDate(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-next-day-ex-date'''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/next-day-ex-date/' + date, token, version)
    return _getJson('ref-data/daily-list/next-day-ex-date', token, version)


def nextDayExtDateDF(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-next-day-ex-date'''
    df = pd.DataFrame(nextDayExtDate(date, token, version))
    _toDatetime(df)
    return df


def directory(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-listed-symbol-directory'''
    if date:
        date = _strOrDate(date)
        return _getJson('ref-data/daily-list/symbol-directory/' + date, token, version)
    return _getJson('ref-data/daily-list/symbol-directory', token, version)


def directoryDF(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-listed-symbol-directory'''
    df = pd.DataFrame(directory(date, token, version))
    _toDatetime(df)
    return df

import pandas as pd
from .common import _getJson


def symbols():
    '''https://iextrading.com/developer/docs/#symbols'''
    return _getJson('ref-data/symbols')


def symbolsDF():
    '''https://iextrading.com/developer/docs/#symbols'''
    return pd.DataFrame(symbols())


def corporateActions():
    '''https://iextrading.com/developer/docs/#iex-corporate-actions'''
    return _getJson('ref-data/daily-list/corporate-actions')


def corporateActionsDF():
    '''https://iextrading.com/developer/docs/#iex-corporate-actions'''
    return pd.DataFrame(corporateActions())


def dividends():
    '''https://iextrading.com/developer/docs/#iex-dividends'''
    return _getJson('ref-data/daily-list/dividends')


def dividendsDF():
    '''https://iextrading.com/developer/docs/#iex-dividends'''
    return pd.DataFrame(dividends())


def nextDayExtDate():
    '''https://iextrading.com/developer/docs/#iex-next-day-ex-date'''
    return _getJson('ref-data/daily-list/next-day-ex-date')


def nextDayExtDateDF():
    '''https://iextrading.com/developer/docs/#iex-next-day-ex-date'''
    return pd.DataFrame(nextDayExtDate())


def directory():
    '''https://iextrading.com/developer/docs/#iex-listed-symbol-directory'''
    return _getJson('ref-data/daily-list/symbol-directory')


def directoryDF():
    '''https://iextrading.com/developer/docs/#iex-listed-symbol-directory'''
    return pd.DataFrame(directory())

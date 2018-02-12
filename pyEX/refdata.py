from .common import _getJson


def symbols():
    '''https://iextrading.com/developer/docs/#symbols'''
    return _getJson('ref-data/symbols')


def corporateActions():
    '''https://iextrading.com/developer/docs/#iex-corporate-actions'''
    return _getJson('ref-data/daily-list/corporate-actions')


def dividends():
    '''https://iextrading.com/developer/docs/#iex-dividends'''
    return _getJson('ref-data/daily-list/dividends')


def nextDayExtDate():
    '''https://iextrading.com/developer/docs/#iex-next-day-ex-date'''
    return _getJson('ref-data/daily-list/next-day-ex-date')


def directory():
    '''https://iextrading.com/developer/docs/#iex-listed-symbol-directory'''
    return _getJson('ref-data/daily-list/symbol-directory')

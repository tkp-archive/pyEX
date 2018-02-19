from ..common import _getJson, _strToList, _raiseIfNotStr, _strOrDate


def tops(symbols=None):
    '''https://iextrading.com/developer/docs/#tops'''
    symbols = _strToList(symbols)
    if symbols:
        return _getJson('tops?symbols=' + ','.join(symbols) + '%2b')
    return _getJson('tops')


def last(symbols=None):
    '''https://iextrading.com/developer/docs/#last'''
    symbols = _strToList(symbols)
    if symbols:
        return _getJson('tops/last?symbols=' + ','.join(symbols) + '%2b')
    return _getJson('tops/last')


def hist(date=None):
    '''https://iextrading.com/developer/docs/#hist'''
    if date is None:
        return _getJson('hist')
    else:
        date = _strOrDate(date)
        return _getJson('hist?date=' + date)


def deep(symbol=None):
    '''https://iextrading.com/developer/docs/#deep'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep?symbols=' + symbol)
    return _getJson('deep')


def book(symbol=None):
    '''https://iextrading.com/developer/docs/#book51'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/book?symbols=' + symbol)
    return _getJson('deep/book')


def trades(symbol=None):
    '''https://iextrading.com/developer/docs/#trades'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trades?symbols=' + symbol)
    return _getJson('deep/trades')


def systemEvent():
    '''https://iextrading.com/developer/docs/#system-event'''
    return _getJson('deep/system-event')


def tradingStatus(symbol=None):
    '''https://iextrading.com/developer/docs/#trading-status'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trading-status?symbols=' + symbol)
    return _getJson('deep/trading-status')


def opHaltStatus(symbol=None):
    '''https://iextrading.com/developer/docs/#operational-halt-status'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/op-halt-status?symbols=' + symbol)
    return _getJson('deep/op-halt-status')


def ssrStatus(symbol=None):
    '''https://iextrading.com/developer/docs/#short-sale-price-test-status'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/ssr-status?symbols=' + symbol)
    return _getJson('deep/ssr-status')


def securityEvent(symbol=None):
    '''https://iextrading.com/developer/docs/#security-event'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/security-event?symbols=' + symbol)
    return _getJson('deep/security-event')


def tradeBreak(symbol=None):
    '''https://iextrading.com/developer/docs/#trade-break'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trade-breaks?symbols=' + symbol)
    return _getJson('deep/trade-breaks')


def auction(symbol=None):
    '''https://iextrading.com/developer/docs/#auction'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/auction?symbols=' + symbol)
    return _getJson('deep/auction')

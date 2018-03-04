import pandas as pd
from ..common import _getJson, _strToList, _raiseIfNotStr, _strOrDate


def tops(symbols=None):
    '''https://iextrading.com/developer/docs/#tops'''
    symbols = _strToList(symbols)
    if symbols:
        return _getJson('tops?symbols=' + ','.join(symbols) + '%2b')
    return _getJson('tops')


def topsDF(symbols=None):
    '''https://iextrading.com/developer/docs/#tops'''
    return pd.io.json.json_normalize(tops(symbols))


def last(symbols=None):
    '''https://iextrading.com/developer/docs/#last'''
    symbols = _strToList(symbols)
    if symbols:
        return _getJson('tops/last?symbols=' + ','.join(symbols) + '%2b')
    return _getJson('tops/last')


def lastDF(symbols=None):
    '''https://iextrading.com/developer/docs/#last'''
    return pd.io.json.json_normalize(last(symbols))


def hist(date=None):
    '''https://iextrading.com/developer/docs/#hist'''
    if date is None:
        return _getJson('hist')
    else:
        date = _strOrDate(date)
        return _getJson('hist?date=' + date)


def histDF(date=None):
    '''https://iextrading.com/developer/docs/#hist'''
    return pd.io.json.json_normalize(hist(date))


def deep(symbol=None):
    '''https://iextrading.com/developer/docs/#deep'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep?symbols=' + symbol)
    return _getJson('deep')


def deepDF(symbol=None):
    '''https://iextrading.com/developer/docs/#deep'''
    return pd.io.json.json_normalize(deep(symbol))


def book(symbol=None):
    '''https://iextrading.com/developer/docs/#book51'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/book?symbols=' + symbol)
    return _getJson('deep/book')


def bookDF(symbol=None):
    '''https://iextrading.com/developer/docs/#book51'''
    return pd.io.json.json_normalize(book(symbol))


def trades(symbol=None):
    '''https://iextrading.com/developer/docs/#trades'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trades?symbols=' + symbol)
    return _getJson('deep/trades')


def tradesDF(symbol=None):
    '''https://iextrading.com/developer/docs/#trades'''
    return pd.io.json.json_normalize(trades(symbol))


def systemEvent():
    '''https://iextrading.com/developer/docs/#system-event'''
    return _getJson('deep/system-event')


def systemEventDF():
    '''https://iextrading.com/developer/docs/#system-event'''
    return pd.io.json.json_normalize(systemEvent())


def tradingStatus(symbol=None):
    '''https://iextrading.com/developer/docs/#trading-status'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trading-status?symbols=' + symbol)
    return _getJson('deep/trading-status')


def tradingStatusDF(symbol=None):
    '''https://iextrading.com/developer/docs/#trading-status'''
    return pd.io.json.json_normalize(tradingStatus(symbol))


def opHaltStatus(symbol=None):
    '''https://iextrading.com/developer/docs/#operational-halt-status'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/op-halt-status?symbols=' + symbol)
    return _getJson('deep/op-halt-status')


def opHaltStatusDF(symbol=None):
    '''https://iextrading.com/developer/docs/#operational-halt-status'''
    return pd.io.json.json_normalize(opHaltStatus(symbol))


def ssrStatus(symbol=None):
    '''https://iextrading.com/developer/docs/#short-sale-price-test-status'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/ssr-status?symbols=' + symbol)
    return _getJson('deep/ssr-status')


def ssrStatusDF(symbol=None):
    '''https://iextrading.com/developer/docs/#short-sale-price-test-status'''
    return pd.io.json.json_normalize(ssrStatus(symbol))


def securityEvent(symbol=None):
    '''https://iextrading.com/developer/docs/#security-event'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/security-event?symbols=' + symbol)
    return _getJson('deep/security-event')


def securityEventDF(symbol=None):
    '''https://iextrading.com/developer/docs/#security-event'''
    return pd.io.json.json_normalize(securityEvent(symbol))


def tradeBreak(symbol=None):
    '''https://iextrading.com/developer/docs/#trade-break'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trade-breaks?symbols=' + symbol)
    return _getJson('deep/trade-breaks')


def tradeBreakDF(symbol=None):
    '''https://iextrading.com/developer/docs/#trade-break'''
    return pd.io.json.json_normalize(tradeBreak(symbol))


def auction(symbol=None):
    '''https://iextrading.com/developer/docs/#auction'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/auction?symbols=' + symbol)
    return _getJson('deep/auction')


def auctionDF(symbol=None):
    '''https://iextrading.com/developer/docs/#auction'''
    return pd.io.json.json_normalize(auction(symbol))

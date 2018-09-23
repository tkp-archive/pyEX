import pandas as pd
from ..common import _getJson, _strToList, _raiseIfNotStr, _strOrDate, _reindex, _toDatetime


def tops(symbols=None):
    '''https://iextrading.com/developer/docs/#tops'''
    symbols = _strToList(symbols)
    if symbols:
        return _getJson('tops?symbols=' + ','.join(symbols) + '%2b')
    return _getJson('tops')


def topsDF(symbols=None):
    '''https://iextrading.com/developer/docs/#tops'''
    df = pd.io.json.json_normalize(tops(symbols))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def last(symbols=None):
    '''https://iextrading.com/developer/docs/#last'''
    symbols = _strToList(symbols)
    if symbols:
        return _getJson('tops/last?symbols=' + ','.join(symbols) + '%2b')
    return _getJson('tops/last')


def lastDF(symbols=None):
    '''https://iextrading.com/developer/docs/#last'''
    df = pd.io.json.json_normalize(last(symbols))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def hist(date=None):
    '''https://iextrading.com/developer/docs/#hist'''
    if date is None:
        return _getJson('hist')
    else:
        date = _strOrDate(date)
        return _getJson('hist?date=' + date)


def histDF(date=None):
    '''https://iextrading.com/developer/docs/#hist'''
    x = hist(date)
    data = []
    for key in x:
        dat = x[key]
        for item in dat:
            item['date'] = key
            data.append(item)
    df = pd.DataFrame(data)
    _toDatetime(df)
    _reindex(df, 'date')
    return df


def deep(symbol=None):
    '''https://iextrading.com/developer/docs/#deep'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep?symbols=' + symbol)
    return _getJson('deep')


def deepDF(symbol=None):
    '''https://iextrading.com/developer/docs/#deep'''
    df = pd.io.json.json_normalize(deep(symbol))
    _toDatetime(df)
    return df


def book(symbol=None):
    '''https://iextrading.com/developer/docs/#book51'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/book?symbols=' + symbol)
    return _getJson('deep/book')


def bookDF(symbol=None):
    '''https://iextrading.com/developer/docs/#book51'''
    x = book(symbol)
    data = []
    for key in x:
        d = x[key]
        d['symbol'] = key
        data.append(d)
    df = pd.io.json.json_normalize(data)
    _toDatetime(df)
    return df


def trades(symbol=None):
    '''https://iextrading.com/developer/docs/#trades'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trades?symbols=' + symbol)
    return _getJson('deep/trades')


def tradesDF(symbol=None):
    '''https://iextrading.com/developer/docs/#trades'''
    x = trades(symbol)
    data = []
    for key in x:
        dat = x[key]
        for d in dat:
            d['symbol'] = key
            data.append(d)
    df = pd.DataFrame(data)
    _toDatetime(df)
    return df


def systemEvent():
    '''https://iextrading.com/developer/docs/#system-event'''
    return _getJson('deep/system-event')


def systemEventDF():
    '''https://iextrading.com/developer/docs/#system-event'''
    df = pd.io.json.json_normalize(systemEvent())
    _toDatetime(df)
    return df


def tradingStatus(symbol=None):
    '''https://iextrading.com/developer/docs/#trading-status'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trading-status?symbols=' + symbol)
    return _getJson('deep/trading-status')


def tradingStatusDF(symbol=None):
    '''https://iextrading.com/developer/docs/#trading-status'''
    x = tradingStatus(symbol)
    data = []
    for key in x:
        d = x[key]
        d['symbol'] = key
        data.append(d)
    df = pd.DataFrame(data)
    _toDatetime(df)
    return df


def opHaltStatus(symbol=None):
    '''https://iextrading.com/developer/docs/#operational-halt-status'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/op-halt-status?symbols=' + symbol)
    return _getJson('deep/op-halt-status')


def opHaltStatusDF(symbol=None):
    '''https://iextrading.com/developer/docs/#operational-halt-status'''
    x = opHaltStatus(symbol)
    data = []
    for key in x:
        d = x[key]
        d['symbol'] = key
        data.append(d)
    df = pd.DataFrame(data)
    _toDatetime(df)
    return df


def ssrStatus(symbol=None):
    '''https://iextrading.com/developer/docs/#short-sale-price-test-status'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/ssr-status?symbols=' + symbol)
    return _getJson('deep/ssr-status')


def ssrStatusDF(symbol=None):
    '''https://iextrading.com/developer/docs/#short-sale-price-test-status'''
    x = ssrStatus(symbol)
    data = []
    for key in x:
        d = x[key]
        d['symbol'] = key
        data.append(d)
    df = pd.DataFrame(data)
    _toDatetime(df)
    return df


def securityEvent(symbol=None):
    '''https://iextrading.com/developer/docs/#security-event'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/security-event?symbols=' + symbol)
    return _getJson('deep/security-event')


def securityEventDF(symbol=None):
    '''https://iextrading.com/developer/docs/#security-event'''
    x = securityEvent(symbol)
    data = []
    for key in x:
        d = x[key]
        d['symbol'] = key
        data.append(d)
    df = pd.DataFrame(data)
    _toDatetime(df)
    return df


def tradeBreak(symbol=None):
    '''https://iextrading.com/developer/docs/#trade-break'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/trade-breaks?symbols=' + symbol)
    return _getJson('deep/trade-breaks')


def tradeBreakDF(symbol=None):
    '''https://iextrading.com/developer/docs/#trade-break'''
    df = pd.io.json.json_normalize(tradeBreak(symbol))
    _toDatetime(df)
    return df


def auction(symbol=None):
    '''https://iextrading.com/developer/docs/#auction'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/auction?symbols=' + symbol)
    return _getJson('deep/auction')


def auctionDF(symbol=None):
    '''https://iextrading.com/developer/docs/#auction'''
    df = pd.io.json.json_normalize(auction(symbol))
    _toDatetime(df)
    return df


def officialPrice(symbol=None):
    '''https://iextrading.com/developer/docs/#official-price'''
    _raiseIfNotStr(symbol)
    if symbol:
        return _getJson('deep/official-price?symbols=' + symbol)
    return _getJson('deep/official-price')


def officialPriceDF(symbol=None):
    '''https://iextrading.com/developer/docs/#official-price'''
    df = pd.io.json.json_normalize(officialPrice(symbol))
    _toDatetime(df)
    return df

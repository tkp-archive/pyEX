# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _expire, _getJson, _raiseIfNotStr, _strOrDate, _reindex, _toDatetime


def crypto(token='', version='', filter=''):
    '''This will return an array of quotes for all Cryptocurrencies supported by the IEX API. Each element is a standard quote object with four additional keys.

    https://iexcloud.io/docs/api/#crypto

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('stock/market/crypto/', token, version, filter)


def cryptoDF(token='', version='', filter=''):
    '''This will return an array of quotes for all Cryptocurrencies supported by the IEX API. Each element is a standard quote object with four additional keys.

    https://iexcloud.io/docs/api/#crypto

    Args:
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(crypto(token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def sentiment(symbol, type='daily', date=None, token='', version='', filter=''):
    '''This endpoint provides social sentiment data from StockTwits. Data can be viewed as a daily value, or by minute for a given date.

    https://iexcloud.io/docs/api/#social-sentiment
    Continuous

    Args:
        symbol (string); Ticker to request
        type (string); 'daily' or 'minute'
        date (string); date in YYYYMMDD or datetime
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/{symbol}/sentiment/{type}/{date}'.format(symbol=symbol, type=type, date=date), token, version, filter)
    return _getJson('stock/{symbol}/sentiment/{type}/'.format(symbol=symbol, type=type), token, version, filter)


def sentimentDF(symbol, type='daily', date=None, token='', version='', filter=''):
    '''This endpoint provides social sentiment data from StockTwits. Data can be viewed as a daily value, or by minute for a given date.

    https://iexcloud.io/docs/api/#social-sentiment
    Continuous

    Args:
        symbol (string); Ticker to request
        type (string); 'daily' or 'minute'
        date (string); date in YYYYMMDD or datetime
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    ret = sentiment(symbol, type, date, token, version, filter)
    if type == 'daily':
        ret = [ret]
    df = pd.DataFrame(ret)
    _toDatetime(df)
    return df


@_expire(hour=1)
def ceoCompensation(symbol, token='', version='', filter=''):
    '''This endpoint provides CEO compensation for a company by symbol.

    https://iexcloud.io/docs/api/#ceo-compensation
    1am daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/{symbol}/ceo-compensation'.format(symbol=symbol), token, version, filter)


def ceoCompensationDF(symbol, token='', version='', filter=''):
    '''This endpoint provides CEO compensation for a company by symbol.

    https://iexcloud.io/docs/api/#ceo-compensation
    1am daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    ret = ceoCompensation(symbol, token, version, filter)
    df = pd.io.json.json_normalize(ret)
    _toDatetime(df)
    return df

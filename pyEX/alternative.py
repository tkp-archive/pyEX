import pandas as pd
from .common import _getJson, _raiseIfNotStr, _strOrDate, _reindex, _toDatetime


def crypto(token='', version=''):
    '''This will return an array of quotes for all Cryptocurrencies supported by the IEX API. Each element is a standard quote object with four additional keys.

    https://iexcloud.io/docs/api/#crypto

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('stock/market/crypto/', token, version)


def cryptoDF(token='', version=''):
    '''This will return an array of quotes for all Cryptocurrencies supported by the IEX API. Each element is a standard quote object with four additional keys.

    https://iexcloud.io/docs/api/#crypto

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(crypto(token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def sentiment(symbol, type='daily', date=None, token='', version=''):
    '''This endpoint provides social sentiment data from StockTwits. Data can be viewed as a daily value, or by minute for a given date.

    https://iexcloud.io/docs/api/#social-sentiment
    Continuous

    Args:
        symbol (string); Ticker to request
        type (string); 'daily' or 'minute'
        date (string); date in YYYYMMDD or datetime
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/{symbol}/sentiment/{type}/{date}'.format(symbol=symbol, type=type, date=date), token, version)
    return _getJson('stock/{symbol}/sentiment/{type}/'.format(symbol=symbol, type=type), token, version)


def sentimentDF(symbol, type='daily', date=None, token='', version=''):
    '''This endpoint provides social sentiment data from StockTwits. Data can be viewed as a daily value, or by minute for a given date.

    https://iexcloud.io/docs/api/#social-sentiment
    Continuous

    Args:
        symbol (string); Ticker to request
        type (string); 'daily' or 'minute'
        date (string); date in YYYYMMDD or datetime
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    ret = sentiment(symbol, type, date, token, version)
    if type == 'daiy':
        ret = [ret]
    df = pd.DataFrame(ret)
    _toDatetime(df)
    return df

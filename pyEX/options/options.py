
# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _getJson, _raiseIfNotStr, _toDatetime


def optionExpirations(symbol, token='', version='', filter=''):
    '''Returns end of day options data

    https://iexcloud.io/docs/api/#options
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/options', token, version, filter)


def options(symbol, expiration, side='', token='', version='', filter=''):
    '''Returns end of day options data

    https://iexcloud.io/docs/api/#options
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (str): Ticker to request
        expiration (str): Expiration date
        side (str): Side (optional)
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if side:
        return _getJson('stock/{symbol}/options/{expiration}/{side}'.format(symbol=symbol, expiration=expiration, side=side), token, version, filter)
    return _getJson('stock/{symbol}/options/{expiration}/'.format(symbol=symbol, expiration=expiration), token, version, filter)


def optionsDF(symbol, expiration, side='', token='', version='', filter=''):
    '''Returns end of day options data

    https://iexcloud.io/docs/api/#options
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (str): Ticker to request
        expiration (str): Expiration date
        side (str): Side (optional)
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    p = options(symbol, expiration, side, token, version, filter)
    df = pd.DataFrame(p)
    _toDatetime(df)
    return df


# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _getJson, _raiseIfNotStr, _toDatetime


def optionExpirations(symbol, token='', version='', filter=''):
    '''Returns end of day options data

    https://iexcloud.io/docs/api/#options
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

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
        symbol (string); Ticker to request
        expiration (string); Expiration date
        side (string); Side (optional)
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

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
        symbol (string); Ticker to request
        expiration (string); Expiration date
        side (string); Side (optional)
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    p = options(symbol, expiration, side, token, version, filter)
    df = pd.DataFrame(p)
    _toDatetime(df)
    return df

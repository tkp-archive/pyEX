# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _getJson, _raiseIfNotStr, _reindex, _toDatetime


def news(symbol, count=10, token='', version='', filter=''):
    '''News about company

    https://iexcloud.io/docs/api/#news
    Continuous

    Args:
        symbol (string); Ticker to request
        count (int): limit number of results
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/news/last/' + str(count), token, version, filter)


def _newsToDF(n):
    '''internal'''
    df = pd.DataFrame(n)
    _toDatetime(df, cols=[], tcols=['datetime'])
    _reindex(df, 'datetime')
    return df


def newsDF(symbol, count=10, token='', version='', filter=''):
    '''News about company

    https://iexcloud.io/docs/api/#news
    Continuous

    Args:
        symbol (string); Ticker to request
        count (int): limit number of results
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    n = news(symbol, count, token, version, filter)
    df = _newsToDF(n)
    return df


def marketNews(count=10, token='', version='', filter=''):
    '''News about market

    https://iexcloud.io/docs/api/#news
    Continuous

    Args:
        count (int): limit number of results
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('stock/market/news/last/' + str(count), token, version, filter)


def marketNewsDF(count=10, token='', version='', filter=''):
    '''News about market

    https://iexcloud.io/docs/api/#news
    Continuous

    Args:
        count (int): limit number of results
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(marketNews(count, token, version, filter))
    _toDatetime(df)
    _reindex(df, 'datetime')
    return df

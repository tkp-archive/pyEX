# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _getJson, _raiseIfNotStr, _toDatetime


def points(symbol='market', key='', token='', version='', filter=''):
    '''Data points are available per symbol and return individual plain text values.
    Retrieving individual data points is useful for Excel and Google Sheet users, and applications where a single, lightweight value is needed.
    We also provide update times for some endpoints which allow you to call an endpoint only once it has new data.


    https://iexcloud.io/docs/api/#data-points

    Args:
        symbol (string); Ticker or market to query
        key (string); data point to fetch. If empty or none, will return available data points
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if key:
        return _getJson('data-points/{symbol}/{key}'.format(symbol=symbol, key=key), token, version, filter)
    return _getJson('data-points/{symbol}'.format(symbol=symbol), token, version, filter)


def pointsDF(symbol='market', key='', token='', version='', filter=''):
    '''Data points are available per symbol and return individual plain text values.
    Retrieving individual data points is useful for Excel and Google Sheet users, and applications where a single, lightweight value is needed.
    We also provide update times for some endpoints which allow you to call an endpoint only once it has new data.


    https://iexcloud.io/docs/api/#data-points

    Args:
        symbol (string); Ticker or market to query
        key (string); data point to fetch. If empty or none, will return available data points
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if key:
        val = points(symbol, key, token, version, filter)
        return pd.DataFrame([{'symbol': symbol, 'key': key, 'value': val}])
    df = pd.DataFrame(points(symbol, key, token, version, filter))
    _toDatetime(df)
    return df

# -*- coding: utf-8 -*-
import pandas as pd
from functools import wraps
from ..common import _getJson, _raiseIfNotStr, _toDatetime


def points(symbol='market', key='', token='', version='', filter=''):
    '''Data points are available per symbol and return individual plain text values.
    Retrieving individual data points is useful for Excel and Google Sheet users, and applications where a single, lightweight value is needed.
    We also provide update times for some endpoints which allow you to call an endpoint only once it has new data.


    https://iexcloud.io/docs/api/#data-points

    Args:
        symbol (str): Ticker or market to query
        key (str): data point to fetch. If empty or none, will return available data points
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    _raiseIfNotStr(symbol)
    if key:
        return _getJson('data-points/{symbol}/{key}'.format(symbol=symbol, key=key), token, version, filter)
    return _getJson('data-points/{symbol}'.format(symbol=symbol), token, version, filter)


@wraps(points)
def pointsDF(symbol='market', key='', token='', version='', filter=''):
    _raiseIfNotStr(symbol)
    if key:
        val = points(symbol, key, token, version, filter)
        return pd.DataFrame([{'symbol': symbol, 'key': key, 'value': val}])
    df = pd.DataFrame(points(symbol, key, token, version, filter))
    _toDatetime(df)
    return df

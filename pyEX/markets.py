import pandas as pd
from .common import _getJson, _toDatetime


def markets(token='', version=''):
    '''https://iextrading.com/developer/docs/#intraday'''
    return _getJson('market', token, version)


def marketsDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#intraday'''
    df = pd.DataFrame(markets(token, version))
    _toDatetime(df)
    return df

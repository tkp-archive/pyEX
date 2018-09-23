import pandas as pd
from .common import _getJson, _toDatetime


def markets():
    '''https://iextrading.com/developer/docs/#intraday'''
    return _getJson('market')


def marketsDF():
    '''https://iextrading.com/developer/docs/#intraday'''
    df = pd.DataFrame(markets())
    _toDatetime(df)
    return df

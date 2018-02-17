import pandas as pd
from .common import _getJson


def markets():
    '''https://iextrading.com/developer/docs/#intraday'''
    return _getJson('market')


def marketsDF():
    '''https://iextrading.com/developer/docs/#intraday'''
    return pd.DataFrame(markets())

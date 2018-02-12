from .common import _getJson


def markets():
    '''https://iextrading.com/developer/docs/#intraday'''
    return _getJson('market')

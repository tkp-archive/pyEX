# -*- coding: utf-8 -*-
from ...common import _expire, _getJson, _strOrDate, PyEXception, _EST


@_expire(hour=10, tz=_EST)
def valuEngineStockResearchReport(symbol='', date=None, token='', version=''):
    '''ValuEngine provides research on over 5,000 stocks with stock valuations, Buy/Hold/Sell recommendations, and forecasted target prices, so that you the individual investor can make informed decisions. Every ValuEngine Valuation and Forecast model for the U.S. equities markets has been extensively back-tested. ValuEngine’s performance exceeds that of many well-known stock-picking styles. Reports available since March 19th, 2020.
    https://iexcloud.io/docs/api/#valuengine-stock-research-report
    '''
    if not symbol or not date:
        raise PyEXception("symbol and date required")
    return _getJson('files/download/VALUENGINE_REPORT?symbol={}&date={}'.format(symbol, _strOrDate(date)), token=token, version=version)

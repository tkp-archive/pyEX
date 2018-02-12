import requests
import pandas as pd
from IPython.display import Image as ImageI
from PIL import Image as ImageP
from io import BytesIO
from .common import _TIMEFRAME_CHART, _TIMEFRAME_DIVSPLIT, _LIST_OPTIONS, _getJson, _df, _raiseIfNotStr


def book(symbol):
    '''https://iextrading.com/developer/docs/#book'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/book')


def chart(symbol, timeframe='1m'):
    '''
    https://iextrading.com/developer/docs/#chart
    https://iextrading.com/developer/docs/#time-series
    '''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_CHART:
        raise Exception('Range must be in %s' % str(_TIMEFRAME_CHART))
    if timeframe:
        return _getJson('stock/' + symbol + '/chart' + '/' + timeframe)
    return _getJson('stock/' + symbol + '/chart')


def chartDF(symbol, timeframe='1m'):
    _raiseIfNotStr(symbol)
    return pd.DataFrame(chart(symbol, timeframe))


def company(symbol):
    '''https://iextrading.com/developer/docs/#company'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/company')


def companyDF(symbol):
    _raiseIfNotStr(symbol)
    return _df(company(symbol))


def delayedQuote(symbol):
    '''https://iextrading.com/developer/docs/#delayed-quote'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/delayed-quote')


def dividends(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#dividends'''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise Exception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/dividends/' + timeframe)


def dividendsDF(symbol, timeframe='ytd'):
    _raiseIfNotStr(symbol)
    return pd.DataFrame(dividends(symbol, timeframe))


def earnings(symbol):
    '''https://iextrading.com/developer/docs/#earnings'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/earnings')


def spread(symbol):
    '''https://iextrading.com/developer/docs/#effective-spread'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/effective-spread')


def spreadDF(symbol):
    _raiseIfNotStr(symbol)
    return pd.DataFrame(spread(symbol))


def financials(symbol):
    '''https://iextrading.com/developer/docs/#financials'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/financials')


def threshhold():
    '''https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list'''
    raise NotImplementedError()


def shortInterest():
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    raise NotImplementedError()


def stockStats(symbol):
    '''https://iextrading.com/developer/docs/#key-stats'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/stats')


def stockStatsDF(symbol):
    _raiseIfNotStr(symbol)
    return _df(stockStats(symbol))


def list(option='mostactive'):
    '''https://iextrading.com/developer/docs/#list'''
    if option not in _LIST_OPTIONS:
        raise Exception('Option must be in %s' % str(_LIST_OPTIONS))
    return _getJson('stock/market/list/' + option)


def listDF(option='mostactive'):
    return pd.DataFrame(list(option))


def logo(symbol):
    '''https://iextrading.com/developer/docs/#logo'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/logo')


def logoPNG(symbol):
    _raiseIfNotStr(symbol)
    response = requests.get(logo(symbol)['url'])
    return ImageP.open(BytesIO(response.content))


def logoNotebook(symbol):
    _raiseIfNotStr(symbol)
    url = logo(symbol)['url']
    return ImageI(url=url)


def news(symbol, count=10):
    '''https://iextrading.com/developer/docs/#news'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/news/last/' + str(count))


def newsDF(symbol, count=10):
    _raiseIfNotStr(symbol)
    return pd.DataFrame(news(symbol, count))


def marketNews(count=10):
    return _getJson('stock/market/news/last/' + str(count))


def marketNewsDF(count=10):
    return pd.DataFrame(marketNews(count))


def ohlc(symbol):
    '''https://iextrading.com/developer/docs/#ohlc'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/ohlc')


def ohlcDF(symbol):
    '''https://iextrading.com/developer/docs/#ohlc'''
    _raiseIfNotStr(symbol)
    return pd.DataFrame(ohlc(symbol))


def marketOhlc():
    return _getJson('stock/market/ohlc')


def marketOhlcDF():
    return pd.DataFrame(marketOhlc())


def peers(symbol):
    '''https://iextrading.com/developer/docs/#peers'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/peers')


def yesterday(symbol):
    '''https://iextrading.com/developer/docs/#previous'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/previous')


def yesterdayDF(symbol):
    _raiseIfNotStr(symbol)
    return _df(yesterday(symbol))


def marketYesterday():
    return _getJson('stock/market/previous')


def marketYesterdayDF():
    return pd.DataFrame(marketYesterday())


def price(symbol):
    '''https://iextrading.com/developer/docs/#price'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/price')


def quote(symbol):
    '''https://iextrading.com/developer/docs/#quote'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/quote')


def quoteDF(symbol):
    _raiseIfNotStr(symbol)
    return _df(quote(symbol))


def relevant(symbol):
    '''https://iextrading.com/developer/docs/#relevant'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/relevant')


def splits(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#splits'''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise Exception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/splits/' + timeframe)


def volumeByVenue(symbol):
    '''https://iextrading.com/developer/docs/#volume-by-venue'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/volume-by-venue')


def volumeByVenueDF(symbol):
    _raiseIfNotStr(symbol)
    return pd.DataFrame(volumeByVenue(symbol))

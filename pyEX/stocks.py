import requests
import pandas as pd
from IPython.display import Image as ImageI
from PIL import Image as ImageP
from io import BytesIO
from .common import _TIMEFRAME_CHART, _TIMEFRAME_DIVSPLIT, _LIST_OPTIONS, _getJson, _raiseIfNotStr, PyEXception, _strOrDate


def book(symbol):
    '''https://iextrading.com/developer/docs/#book'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/book')


def bookDF(symbol):
    '''https://iextrading.com/developer/docs/#book'''
    return pd.io.json.json_normalize(book(symbol))


def chart(symbol, timeframe='1m', date=None):
    '''
    https://iextrading.com/developer/docs/#chart
    https://iextrading.com/developer/docs/#time-series
    '''
    _raiseIfNotStr(symbol)
    if timeframe:
        if timeframe not in _TIMEFRAME_CHART:
            raise PyEXception('Range must be in %s' % str(_TIMEFRAME_CHART))
        return _getJson('stock/' + symbol + '/chart' + '/' + timeframe)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/' + symbol + '/chart' + '/date/' + date)
    return _getJson('stock/' + symbol + '/chart')


def chartDF(symbol, timeframe='1m'):
    '''
    https://iextrading.com/developer/docs/#chart
    https://iextrading.com/developer/docs/#time-series
    '''
    return pd.DataFrame(chart(symbol, timeframe))


def company(symbol):
    '''https://iextrading.com/developer/docs/#company'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/company')


def companyDF(symbol):
    '''https://iextrading.com/developer/docs/#company'''
    return pd.io.json.json_normalize(company(symbol))


def delayedQuote(symbol):
    '''https://iextrading.com/developer/docs/#delayed-quote'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/delayed-quote')


def delayedQuoteDF(symbol):
    '''https://iextrading.com/developer/docs/#delayed-quote'''
    return pd.io.json.json_normalize(delayedQuote(symbol))


def dividends(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#dividends'''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/dividends/' + timeframe)


def dividendsDF(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#dividends'''
    return pd.DataFrame(dividends(symbol, timeframe))


def earnings(symbol):
    '''https://iextrading.com/developer/docs/#earnings'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/earnings')


def earningsDF(symbol):
    '''https://iextrading.com/developer/docs/#earnings'''
    return pd.DataFrame(earnings(symbol))


def spread(symbol):
    '''https://iextrading.com/developer/docs/#effective-spread'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/effective-spread')


def spreadDF(symbol):
    '''https://iextrading.com/developer/docs/#effective-spread'''
    return pd.DataFrame(spread(symbol))


def financials(symbol):
    '''https://iextrading.com/developer/docs/#financials'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/financials')


def financialsDF(symbol):
    '''https://iextrading.com/developer/docs/#financials'''
    return pd.DataFrame(financials(symbol))


def threshold(date=None):
    '''https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list'''
    if date:
        date = _strOrDate(date)
        return _getJson('stock/market/threshold-securities/' + date)
    return _getJson('stock/market/threshold-securities')


def thresholdDF(date=None):
    '''https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list'''
    return pd.DataFrame(threshold(date))


def shortInterest(symbol, date=None):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    _raiseIfNotStr(symbol)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/' + symbol + '/short-interest/' + date)
    return _getJson('stock/' + symbol + '/short-interest')


def shortInterestDF(symbol, date=None):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    return pd.DataFrame(shortInterest(symbol, date))


def marketShortInterest(date=None):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    if date:
        date = _strOrDate(date)
        return _getJson('stock/market/short-interest/' + date)
    return _getJson('stock/market/short-interest')


def marketShortInterestDF(date=None):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    return pd.DataFrame(marketShortInterest(date))


def stockStats(symbol):
    '''https://iextrading.com/developer/docs/#key-stats'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/stats')


def stockStatsDF(symbol):
    '''https://iextrading.com/developer/docs/#key-stats'''
    return pd.io.json.json_normalize(stockStats(symbol))


def list(option='mostactive'):
    '''https://iextrading.com/developer/docs/#list'''
    if option not in _LIST_OPTIONS:
        raise PyEXception('Option must be in %s' % str(_LIST_OPTIONS))
    return _getJson('stock/market/list/' + option)


def listDF(option='mostactive'):
    '''https://iextrading.com/developer/docs/#list'''
    return pd.DataFrame(list(option))


def logo(symbol):
    '''https://iextrading.com/developer/docs/#logo'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/logo')


def logoPNG(symbol):
    '''https://iextrading.com/developer/docs/#logo'''
    _raiseIfNotStr(symbol)
    response = requests.get(logo(symbol)['url'])
    return ImageP.open(BytesIO(response.content))


def logoNotebook(symbol):
    '''https://iextrading.com/developer/docs/#logo'''
    _raiseIfNotStr(symbol)
    url = logo(symbol)['url']
    return ImageI(url=url)


def news(symbol, count=10):
    '''https://iextrading.com/developer/docs/#news'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/news/last/' + str(count))


def newsDF(symbol, count=10):
    '''https://iextrading.com/developer/docs/#news'''
    return pd.DataFrame(news(symbol, count))


def marketNews(count=10):
    '''https://iextrading.com/developer/docs/#news'''
    return _getJson('stock/market/news/last/' + str(count))


def marketNewsDF(count=10):
    '''https://iextrading.com/developer/docs/#news'''
    return pd.DataFrame(marketNews(count))


def ohlc(symbol):
    '''https://iextrading.com/developer/docs/#ohlc'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/ohlc')


def ohlcDF(symbol):
    '''https://iextrading.com/developer/docs/#ohlc'''
    return pd.DataFrame(ohlc(symbol))


def marketOhlc():
    '''https://iextrading.com/developer/docs/#ohlc'''
    return _getJson('stock/market/ohlc')


def marketOhlcDF():
    '''https://iextrading.com/developer/docs/#ohlc'''
    return pd.DataFrame(marketOhlc())


def peers(symbol):
    '''https://iextrading.com/developer/docs/#peers'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/peers')


def peersDF(symbol):
    '''https://iextrading.com/developer/docs/#peers'''
    return pd.DataFrame(peers(symbol))


def yesterday(symbol):
    '''https://iextrading.com/developer/docs/#previous'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/previous')


def yesterdayDF(symbol):
    '''https://iextrading.com/developer/docs/#previous'''
    return pd.io.json.json_normalize(yesterday(symbol))


def marketYesterday():
    '''https://iextrading.com/developer/docs/#previous'''
    return _getJson('stock/market/previous')


def marketYesterdayDF():
    '''https://iextrading.com/developer/docs/#previous'''
    return pd.DataFrame(marketYesterday())


def price(symbol):
    '''https://iextrading.com/developer/docs/#price'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/price')


def priceDF(symbol):
    '''https://iextrading.com/developer/docs/#price'''
    return pd.io.json.json_normalize({'price': price(symbol)})


def quote(symbol):
    '''https://iextrading.com/developer/docs/#quote'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/quote')


def quoteDF(symbol):
    '''https://iextrading.com/developer/docs/#quote'''
    return pd.io.json.json_normalize(quote(symbol))


def relevant(symbol):
    '''https://iextrading.com/developer/docs/#relevant'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/relevant')


def relevantDF(symbol):
    '''https://iextrading.com/developer/docs/#relevant'''
    return pd.DataFrame(relevant(symbol))


def splits(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#splits'''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/splits/' + timeframe)


def splitsDF(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#splits'''
    return pd.DataFrame(splits(symbol, timeframe))


def volumeByVenue(symbol):
    '''https://iextrading.com/developer/docs/#volume-by-venue'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/volume-by-venue')


def volumeByVenueDF(symbol):
    '''https://iextrading.com/developer/docs/#volume-by-venue'''
    return pd.DataFrame(volumeByVenue(symbol))

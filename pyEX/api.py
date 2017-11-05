import requests
import pandas as pd
from IPython.display import Image as ImageI
from PIL import Image as ImageP
from io import BytesIO


_URL_PREFIX = 'https://api.iextrading.com/1.0/'
_TIMEFRAME_CHART = ['', '5y', '2y', '1y', 'ytd', '6m', '3m', '1m', '1d']
_TIMEFRAME_DIVSPLIT = ['5y', '2y', '1y', 'ytd', '6m', '3m', '1m']
_LIST_OPTIONS = ['mostactive', 'gainers', 'losers', 'iexvolume', 'iexpercent']


def _getJson(url):
    url = _URL_PREFIX + url
    resp = requests.get(url)
    if resp.status_code == 200:
        return resp.json()
    raise Exception('Response %d - ' % resp.status_code, resp.text)


def _df(resp):
    df = {k: [v] for k, v in resp.items()}
    return pd.DataFrame(df)


def company(symbol):
    return _getJson('stock/' + symbol + '/company')


def companyDF(symbol):
    return _df(company(symbol))


def quote(symbol):
    return _getJson('stock/' + symbol + '/quote')


def quoteDF(symbol):
    return _df(quote(symbol))


def price(symbol):
    return _getJson('stock/' + symbol + '/price')


def spread(symbol):
    return _getJson('stock/' + symbol + '/effective-spread')


def spreadDF(symbol):
    return pd.DataFrame(spread(symbol))


def volumeByVenue(symbol):
    return _getJson('stock/' + symbol + '/volume-by-venue')


def volumeByVenueDF(symbol):
    return pd.DataFrame(volumeByVenue(symbol))


def delayedQuote(symbol):
    return _getJson('stock/' + symbol + '/delayed-quote')


def yesterday(symbol):
    return _getJson('stock/' + symbol + '/previous')


def yesterdayDF(symbol):
    return _df(yesterday(symbol))


def marketYesterday():
    return _getJson('stock/market/previous')


def marketYesterdayDF():
    return pd.DataFrame(marketYesterday())


def book(symbol):
    return _getJson('stock/' + symbol + '/book')


def openClose(symbol):
    return _getJson('stock/' + symbol + '/open-close')


def marketOpenClose():
    return _getJson('stock/market/open-close')


def stats(symbol):
    return _getJson('stock/' + symbol + '/stats')


def statsDF(symbol):
    return _df(stats(symbol))


def financials(symbol):
    return _getJson('stock/' + symbol + '/financials')


def earnings(symbol):
    return _getJson('stock/' + symbol + '/earnings')


def peers(symbol):
    return _getJson('stock/' + symbol + '/peers')


def relevant(symbol):
    return _getJson('stock/' + symbol + '/relevant')


def dividends(symbol, timeframe='ytd'):
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise Exception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/dividends/' + timeframe)


def dividendsDF(symbol, timeframe='ytd'):
    return pd.DataFrame(dividends(symbol, timeframe))


def splits(symbol, timeframe='ytd'):
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise Exception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/splits/' + timeframe)


def news(symbol, count=10):
    return _getJson('stock/' + symbol + '/news/last/' + str(count))


def newsDF(symbol, count=10):
    return pd.DataFrame(news(symbol, count))


def marketNews(count=10):
    return _getJson('stock/market/news/last/' + str(count))


def marketNewsDF(count=10):
    return pd.DataFrame(marketNews(count))


def chart(symbol, timeframe=''):
    if timeframe not in _TIMEFRAME_CHART:
        raise Exception('Range must be in %s' % str(_TIMEFRAME_CHART))
    if timeframe:
        return _getJson('stock/' + symbol + '/chart' + '/' + timeframe)
    return _getJson('stock/' + symbol + '/chart')


def logo(symbol):
    return _getJson('stock/' + symbol + '/logo')


def logoPNG(symbol):
    response = requests.get(logo(symbol)['url'])
    return ImageP.open(BytesIO(response.content))


def logoNotebook(symbol):
    url = logo(symbol)['url']
    return ImageI(url=url)


def list(option='mostactive'):
    if option not in _LIST_OPTIONS:
        raise Exception('Option must be in %s' % str(_LIST_OPTIONS))
    return _getJson('stock/market/list/' + option)


def listDF(option='mostactive'):
    return pd.DataFrame(list(option))

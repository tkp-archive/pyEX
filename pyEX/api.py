import requests

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


def company(symbol):
    return _getJson('stock/' + symbol + '/company')


def quote(symbol):
    return _getJson('stock/' + symbol + '/quote')


def price(symbol):
    return _getJson('stock/' + symbol + '/price')


def spread(symbol):
    return _getJson('stock/' + symbol + '/effective-spread')


def volumeByVenue(symbol):
    return _getJson('stock/' + symbol + '/volume-by-venue')


def delayedQuote(symbol):
    return _getJson('stock/' + symbol + '/delayed-quote')


def yesterday(symbol):
    return _getJson('stock/' + symbol + '/previous')


def marketYesterday():
    return _getJson('stock/market/previous')


def book(symbol):
    return _getJson('stock/' + symbol + '/book')


def openClose(symbol):
    return _getJson('stock/' + symbol + '/open-close')


def marketOpenClose():
    return _getJson('stock/market/open-close')


def stats(symbol):
    return _getJson('stock/' + symbol + '/stats')


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


def splits(symbol, timeframe='ytd'):
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise Exception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/splits/' + timeframe)


def news(symbol, count=10):
    return _getJson('stock/' + symbol + '/news/last/' + str(count))


def marketNews(count=10):
    return _getJson('stock/market/news/last/' + str(count))


def chart(symbol, timeframe=''):
    if timeframe not in _TIMEFRAME_CHART:
        raise Exception('Range must be in %s' % str(_TIMEFRAME_CHART))
    if timeframe:
        return _getJson('stock/' + symbol + '/chart' + '/' + timeframe)
    return _getJson('stock/' + symbol + '/chart')


def logo(symbol):
    return _getJson('stock/' + symbol + '/logo')


def list(option='mostactive'):
    if option not in _LIST_OPTIONS:
        raise Exception('Option must be in %s' % str(_LIST_OPTIONS))
    return _getJson('stock/market/list/' + option)

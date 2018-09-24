import requests
import pandas as pd
from IPython.display import Image as ImageI
from PIL import Image as ImageP
from io import BytesIO
from .common import _TIMEFRAME_CHART, _TIMEFRAME_DIVSPLIT, _LIST_OPTIONS, _COLLECTION_TAGS, _getJson, _raiseIfNotStr, PyEXception, _strOrDate, _reindex, _toDatetime


def book(symbol):
    '''https://iextrading.com/developer/docs/#book'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/book')


def bookDF(symbol):
    '''https://iextrading.com/developer/docs/#book'''
    x = book(symbol)
    quote = x.get('quote', [])
    asks = x.get('asks', [])
    bids = x.get('bids', [])
    trades = x.get('trades', [])

    df1 = pd.io.json.json_normalize(quote)
    df1['type'] = 'quote'

    df2 = pd.io.json.json_normalize(asks)
    df2['symbol'] = quote['symbol']
    df2['type'] = 'ask'

    df3 = pd.io.json.json_normalize(bids)
    df3['symbol'] = quote['symbol']
    df3['type'] = 'bid'

    df4 = pd.io.json.json_normalize(trades)
    df4['symbol'] = quote['symbol']
    df3['type'] = 'trade'

    df = pd.concat([df1, df2, df3, df4], sort=True)
    _toDatetime(df)
    return df


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


def chartDF(symbol, timeframe='1m', date=None):
    '''
    https://iextrading.com/developer/docs/#chart
    https://iextrading.com/developer/docs/#time-series
    '''
    df = pd.DataFrame(chart(symbol, timeframe, date))
    _toDatetime(df)
    if timeframe is not None and timeframe != '1d':
        _reindex(df, 'date')
    else:
        if not df.empty:
            df.set_index(['date', 'minute'], inplace=True)
        else:
            return pd.DataFrame()
    return df


def company(symbol):
    '''https://iextrading.com/developer/docs/#company'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/company')


def companyDF(symbol):
    '''https://iextrading.com/developer/docs/#company'''
    df = pd.io.json.json_normalize(company(symbol))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def collections(tag, collectionName):
    '''https://iextrading.com/developer/docs/#collections'''
    if tag not in _COLLECTION_TAGS:
        raise PyEXception('Tag must be in %s' % str(_COLLECTION_TAGS))
    return _getJson('stock/market/collection/' + tag + '?collectionName=' + collectionName)


def collectionsDF(tag, query):
    '''https://iextrading.com/developer/docs/#collections'''
    df = pd.DataFrame(collections(tag, query))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def crypto():
    '''https://iextrading.com/developer/docs/#collections'''
    return _getJson('stock/market/crypto/')


def cryptoDF():
    '''https://iextrading.com/developer/docs/#collections'''
    df = pd.DataFrame(crypto())
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def delayedQuote(symbol):
    '''https://iextrading.com/developer/docs/#delayed-quote'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/delayed-quote')


def delayedQuoteDF(symbol):
    '''https://iextrading.com/developer/docs/#delayed-quote'''
    df = pd.io.json.json_normalize(delayedQuote(symbol))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def dividends(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#dividends'''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/dividends/' + timeframe)


def dividendsDF(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#dividends'''
    df = pd.DataFrame(dividends(symbol, timeframe))
    _toDatetime(df)
    _reindex(df, 'exDate')
    return df


def earnings(symbol):
    '''https://iextrading.com/developer/docs/#earnings'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/earnings')


def earningsDF(symbol):
    '''https://iextrading.com/developer/docs/#earnings'''
    df = pd.io.json.json_normalize(earnings(symbol), 'earnings', 'symbol')
    _toDatetime(df)
    _reindex(df, 'EPSReportDate')
    return df


def earningsToday():
    '''https://iextrading.com/developer/docs/#earnings-today'''
    return _getJson('stock/market/today-earnings')


def earningsTodayDF():
    '''https://iextrading.com/developer/docs/#earnings-today'''
    x = earningsToday()
    z = []
    for k in x:
        ds = x[k]
        for d in ds:
            d['when'] = k
            z.extend(ds)
    df = pd.io.json.json_normalize(z)

    if not df.empty:
        df.drop_duplicates(inplace=True)

    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def spread(symbol):
    '''https://iextrading.com/developer/docs/#effective-spread'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/effective-spread')


def spreadDF(symbol):
    '''https://iextrading.com/developer/docs/#effective-spread'''
    df = pd.DataFrame(spread(symbol))
    _toDatetime(df)
    _reindex(df, 'venue')
    return df


def financials(symbol):
    '''https://iextrading.com/developer/docs/#financials'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/financials')


def financialsDF(symbol):
    '''https://iextrading.com/developer/docs/#financials'''
    df = pd.io.json.json_normalize(financials(symbol), 'financials', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    return df


def ipoToday():
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    return _getJson('stock/market/today-ipos')


def ipoTodayDF():
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    val = ipoToday()
    df = pd.io.json.json_normalize(val, 'rawData')
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def ipoUpcoming():
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    return _getJson('stock/market/upcoming-ipos')


def ipoUpcomingDF():
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    val = ipoUpcoming()
    df = pd.io.json.json_normalize(val, 'rawData')
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def threshold(date=None):
    '''https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list'''
    if date:
        date = _strOrDate(date)
        return _getJson('stock/market/threshold-securities/' + date)
    return _getJson('stock/market/threshold-securities')


def thresholdDF(date=None):
    '''https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list'''
    df = pd.DataFrame(threshold(date))
    _toDatetime(df)
    return df


def shortInterest(symbol, date=None):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    _raiseIfNotStr(symbol)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/' + symbol + '/short-interest/' + date)
    return _getJson('stock/' + symbol + '/short-interest')


def shortInterestDF(symbol, date=None):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    df = pd.DataFrame(shortInterest(symbol, date))
    _toDatetime(df)
    return df


def marketShortInterest(date=None):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    if date:
        date = _strOrDate(date)
        return _getJson('stock/market/short-interest/' + date)
    return _getJson('stock/market/short-interest')


def marketShortInterestDF(date=None):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    df = pd.DataFrame(marketShortInterest(date))
    _toDatetime(df)
    return df


def stockStats(symbol):
    '''https://iextrading.com/developer/docs/#key-stats'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/stats')


def stockStatsDF(symbol):
    '''https://iextrading.com/developer/docs/#key-stats'''
    df = pd.io.json.json_normalize(stockStats(symbol))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def largestTrades(symbol):
    '''https://iextrading.com/developer/docs/#largest-trades'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/largest-trades')


def largestTradesDF(symbol):
    '''https://iextrading.com/developer/docs/#largest-trades'''
    df = pd.DataFrame(largestTrades(symbol))
    _toDatetime(df)
    _reindex(df, 'time')
    return df


def list(option='mostactive'):
    '''https://iextrading.com/developer/docs/#list'''
    if option not in _LIST_OPTIONS:
        raise PyEXception('Option must be in %s' % str(_LIST_OPTIONS))
    return _getJson('stock/market/list/' + option)


def listDF(option='mostactive'):
    '''https://iextrading.com/developer/docs/#list'''
    df = pd.DataFrame(list(option))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


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
    df = pd.DataFrame(news(symbol, count))
    _toDatetime(df)
    _reindex(df, 'datetime')
    return df


def marketNews(count=10):
    '''https://iextrading.com/developer/docs/#news'''
    return _getJson('stock/market/news/last/' + str(count))


def marketNewsDF(count=10):
    '''https://iextrading.com/developer/docs/#news'''
    df = pd.DataFrame(marketNews(count))
    _toDatetime(df)
    _reindex(df, 'datetime')
    return df


def ohlc(symbol):
    '''https://iextrading.com/developer/docs/#ohlc'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/ohlc')


def ohlcDF(symbol):
    '''https://iextrading.com/developer/docs/#ohlc'''
    df = pd.io.json.json_normalize(ohlc(symbol))
    _toDatetime(df)
    return df


def marketOhlc():
    '''https://iextrading.com/developer/docs/#ohlc'''
    return _getJson('stock/market/ohlc')


def marketOhlcDF():
    '''https://iextrading.com/developer/docs/#ohlc'''
    x = marketOhlc()
    data = []
    for key in x:
        data.append(x[key])
        data[-1]['symbol'] = key
    df = pd.io.json.json_normalize(data)
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def peers(symbol):
    '''https://iextrading.com/developer/docs/#peers'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/peers')


def peersDF(symbol):
    '''https://iextrading.com/developer/docs/#peers'''
    df = pd.DataFrame(peers(symbol), columns=['symbol'])
    _toDatetime(df)
    _reindex(df, 'symbol')
    df['peer'] = df.index
    return df


def yesterday(symbol):
    '''https://iextrading.com/developer/docs/#previous'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/previous')


def yesterdayDF(symbol):
    '''https://iextrading.com/developer/docs/#previous'''
    df = pd.io.json.json_normalize(yesterday(symbol))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def marketYesterday():
    '''https://iextrading.com/developer/docs/#previous'''
    return _getJson('stock/market/previous')


def marketYesterdayDF():
    '''https://iextrading.com/developer/docs/#previous'''
    x = marketYesterday()
    data = []
    for key in x:
        data.append(x[key])
        data[-1]['symbol'] = key
    df = pd.DataFrame(data)
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def price(symbol):
    '''https://iextrading.com/developer/docs/#price'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/price')


def priceDF(symbol):
    '''https://iextrading.com/developer/docs/#price'''
    df = pd.io.json.json_normalize({'price': price(symbol)})
    _toDatetime(df)
    return df


def quote(symbol):
    '''https://iextrading.com/developer/docs/#quote'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/quote')


def quoteDF(symbol):
    '''https://iextrading.com/developer/docs/#quote'''
    df = pd.io.json.json_normalize(quote(symbol))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def relevant(symbol):
    '''https://iextrading.com/developer/docs/#relevant'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/relevant')


def relevantDF(symbol):
    '''https://iextrading.com/developer/docs/#relevant'''
    df = pd.DataFrame(relevant(symbol))
    _toDatetime(df)
    return df


def sectorPerformance():
    '''https://iextrading.com/developer/docs/#sector-performance'''
    return _getJson('stock/market/sector-performance')


def sectorPerformanceDF():
    '''https://iextrading.com/developer/docs/#sector-performance'''
    df = pd.DataFrame(sectorPerformance())
    _toDatetime(df)
    _reindex(df, 'name')
    return df


def splits(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#splits'''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/splits/' + timeframe)


def splitsDF(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#splits'''
    df = pd.DataFrame(splits(symbol, timeframe))
    _toDatetime(df)
    _reindex(df, 'exDate')
    return df


def volumeByVenue(symbol):
    '''https://iextrading.com/developer/docs/#volume-by-venue'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/volume-by-venue')


def volumeByVenueDF(symbol):
    '''https://iextrading.com/developer/docs/#volume-by-venue'''
    df = pd.DataFrame(volumeByVenue(symbol))
    _toDatetime(df)
    _reindex(df, 'venue')
    return df

import itertools
import requests
import pandas as pd
from io import BytesIO
from IPython.display import Image as ImageI
from multiprocessing.pool import ThreadPool
from PIL import Image as ImageP
from .common import _TIMEFRAME_CHART, _TIMEFRAME_DIVSPLIT, _LIST_OPTIONS, _COLLECTION_TAGS, _getJson, _raiseIfNotStr, PyEXception, _strOrDate, _reindex, _toDatetime, _BATCH_TYPES


def batch(symbols, types=None, _range='1m', last=10):
    '''fetch a large number of fields at the same time'''
    types = types or _BATCH_TYPES

    if not isinstance(symbols, [].__class__):
        if not isinstance(symbols, str):
            raise PyEXception('batch expects string or list of strings for symbols argument')

    if isinstance(types, str):
        types = [types]

    if _range not in _TIMEFRAME_CHART:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_CHART))

    if isinstance(symbols, str):
        route = 'stock/{}/batch?types={}&range={}&last={}'.format(symbols, ','.join(types), _range, last)
        return _getJson(route)

    if len(symbols) > 100:
        raise PyEXception('IEX will only handle up to 100 symbols at a time!')
    route = 'stock/market/batch?symbols={}&types={}&range={}&last={}'.format(','.join(symbols), ','.join(types), _range, last)
    return _getJson(route)


def batchDF(symbols, types=None, _range='1m', last=10):
    '''fetch a large number of fields at the same time'''
    x = batch(symbols, types, _range, last)

    ret = {}

    if isinstance(symbols, str):
        for field in x.keys():
            ret[field] = _MAPPING[field](x[field])
    else:
        for symbol in x.keys():
            for field in x[symbol].keys():
                if field not in ret:
                    ret[field] = pd.DataFrame()

                dat = x[symbol][field]
                dat = _MAPPING[field](dat)
                dat['KEY'] = symbol

                ret[field] = pd.concat([ret[field], dat], sort=True)
    return ret


def bulkBatch(symbols, types=None, _range='1m', last=10):
    '''fetch a large number of fields for multiple symbols all at the same time'''
    types = types or _BATCH_TYPES
    args = []
    empty_data = []
    list_orig = empty_data.__class__

    if not isinstance(symbols, list_orig):
        raise PyEXception('Symbols must be of type list')

    for i in range(0, len(symbols), 99):
        args.append((symbols[i:i+99], types, _range, last))

    pool = ThreadPool(20)
    rets = pool.starmap(batch, args)
    pool.close()

    ret = {}

    for i, d in enumerate(rets):
        symbols_subset = args[i][0]
        if len(d) != len(symbols_subset):
            empty_data.extend(list_orig(set(symbols_subset) - set(d.keys())))
        ret.update(d)

    for k in empty_data:
        if k not in ret:
            if isinstance(types, str):
                ret[k] = {}
            else:
                ret[k] = {x: {} for x in types}
    return ret


def bulkBatchDF(symbols, types=None, _range='1m', last=10):
    '''fetch a large number of fields for multiple symbols all at the same time'''
    dat = bulkBatch(symbols, types, _range, last)
    ret = {}
    for symbol in dat:
        for field in dat[symbol]:
            if field not in ret:
                ret[field] = pd.DataFrame()

            d = dat[symbol][field]
            d = _MAPPING[field](d)
            d['KEY'] = symbol
            ret[field] = pd.concat([ret[field], d], sort=True)

    return ret


def book(symbol):
    '''https://iextrading.com/developer/docs/#book'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/book')


def _bookToDF(b):
    quote = b.get('quote', [])
    asks = b.get('asks', [])
    bids = b.get('bids', [])
    trades = b.get('trades', [])

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


def bookDF(symbol):
    '''https://iextrading.com/developer/docs/#book'''
    x = book(symbol)
    df = _bookToDF(x)
    return df


def chart(symbol, timeframe='1m', date=None):
    '''
    https://iextrading.com/developer/docs/#chart
    https://iextrading.com/developer/docs/#time-series
    '''
    _raiseIfNotStr(symbol)
    if timeframe is not None and timeframe != '1d':
        if timeframe not in _TIMEFRAME_CHART:
            raise PyEXception('Range must be in %s' % str(_TIMEFRAME_CHART))
        return _getJson('stock/' + symbol + '/chart' + '/' + timeframe)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/' + symbol + '/chart' + '/date/' + date)
    return _getJson('stock/' + symbol + '/chart')


def _chartToDF(c):
    df = pd.DataFrame(c)
    _toDatetime(df)
    _reindex(df, 'date')
    return df


def chartDF(symbol, timeframe='1m', date=None):
    '''
    https://iextrading.com/developer/docs/#chart
    https://iextrading.com/developer/docs/#time-series
    '''
    c = chart(symbol, timeframe, date)
    df = pd.DataFrame(c)
    _toDatetime(df)
    if timeframe is not None and timeframe != '1d':
        _reindex(df, 'date')
    else:
        if not df.empty:
            df.set_index(['date', 'minute'], inplace=True)
        else:
            return pd.DataFrame()
    return df


def bulkMinuteBars(symbol, dates):
    '''fetch many dates worth of minute-bars for a given symbol'''
    _raiseIfNotStr(symbol)
    dates = [_strOrDate(date) for date in dates]
    list_orig = dates.__class__

    args = []
    for date in dates:
        args.append((symbol, '1d', date))

    pool = ThreadPool(20)
    rets = pool.starmap(chart, args)
    pool.close()

    return list_orig(itertools.chain(*rets))


def bulkMinuteBarsDF(symbol, dates):
    '''fetch many dates worth of minute-bars for a given symbol'''
    data = bulkMinuteBars(symbol, dates)
    df = pd.DataFrame(data)
    if df.empty:
        return df
    _toDatetime(df)
    df.set_index(['date', 'minute'], inplace=True)
    return df


def company(symbol):
    '''https://iextrading.com/developer/docs/#company'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/company')


def _companyToDF(c):
    df = pd.io.json.json_normalize(c)
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def companyDF(symbol):
    '''https://iextrading.com/developer/docs/#company'''
    c = company(symbol)
    df = _companyToDF(c)
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


def _dividendsToDF(d):
    df = pd.DataFrame(d)
    _toDatetime(df)
    _reindex(df, 'exDate')
    return df


def dividendsDF(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#dividends'''
    d = dividends(symbol, timeframe)
    df = _dividendsToDF(d)
    return df


def earnings(symbol):
    '''https://iextrading.com/developer/docs/#earnings'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/earnings')


def _earningsToDF(e):
    if e:
        df = pd.io.json.json_normalize(e, 'earnings', 'symbol')
        _toDatetime(df)
        _reindex(df, 'EPSReportDate')
    else:
        df = pd.DataFrame()
    return df


def earningsDF(symbol):
    '''https://iextrading.com/developer/docs/#earnings'''
    e = earnings(symbol)
    df = _earningsToDF(e)
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


def _financialsToDF(f):
    if f:
        df = pd.io.json.json_normalize(f, 'financials', 'symbol')
        _toDatetime(df)
        _reindex(df, 'reportDate')
    else:
        df = pd.DataFrame()
    return df


def financialsDF(symbol):
    '''https://iextrading.com/developer/docs/#financials'''
    f = financials(symbol)
    df = _financialsToDF(f)
    return df


def ipoToday():
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    return _getJson('stock/market/today-ipos')


def ipoTodayDF():
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    val = ipoToday()
    if val:
        df = pd.io.json.json_normalize(val, 'rawData')
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def ipoUpcoming():
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    return _getJson('stock/market/upcoming-ipos')


def ipoUpcomingDF():
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    val = ipoUpcoming()
    if val:
        df = pd.io.json.json_normalize(val, 'rawData')
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
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


def _statsToDF(s):
    if s:
        df = pd.io.json.json_normalize(s)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def stockStatsDF(symbol):
    '''https://iextrading.com/developer/docs/#key-stats'''
    s = stockStats(symbol)
    df = _statsToDF(s)
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


def _newsToDF(n):
    df = pd.DataFrame(n)
    _toDatetime(df)
    _reindex(df, 'datetime')
    return df


def newsDF(symbol, count=10):
    '''https://iextrading.com/developer/docs/#news'''
    n = news(symbol, count)
    df = _newsToDF(n)
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
    o = ohlc(symbol)
    if o:
        df = pd.io.json.json_normalize(o)
        _toDatetime(df)
    else:
        df = pd.DataFrame()
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


def _peersToDF(p):
    df = pd.DataFrame(p, columns=['symbol'])
    _toDatetime(df)
    _reindex(df, 'symbol')
    df['peer'] = df.index
    return df


def peersDF(symbol):
    '''https://iextrading.com/developer/docs/#peers'''
    p = peers(symbol)
    df = _peersToDF(p)
    return df


def yesterday(symbol):
    '''https://iextrading.com/developer/docs/#previous'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/previous')


def yesterdayDF(symbol):
    '''https://iextrading.com/developer/docs/#previous'''
    y = yesterday(symbol)
    if y:
        df = pd.io.json.json_normalize(y)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
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
    q = quote(symbol)
    if q:
        df = pd.io.json.json_normalize(q)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
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


def _splitsToDF(s):
    df = pd.DataFrame(s)
    _toDatetime(df)
    _reindex(df, 'exDate')
    return df


def splitsDF(symbol, timeframe='ytd'):
    '''https://iextrading.com/developer/docs/#splits'''
    s = splits(symbol, timeframe)
    df = _splitsToDF(s)
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

_MAPPING = {
    'book': _bookToDF,
    'chart': _chartToDF,
    'company': _companyToDF,
    'dividends': _dividendsToDF,
    'earnings': _earningsToDF,
    'financials': _financialsToDF,
    'stats': _statsToDF,
    'news': _newsToDF,
    'peers': _peersToDF,
    'splits': _splitsToDF,
}

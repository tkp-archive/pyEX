import itertools
import requests
import pandas as pd
from io import BytesIO
from IPython.display import Image as ImageI
from multiprocessing.pool import ThreadPool
from PIL import Image as ImageP
from .common import _TIMEFRAME_CHART, _TIMEFRAME_DIVSPLIT, _LIST_OPTIONS, _COLLECTION_TAGS, _getJson, _raiseIfNotStr, PyEXception, _strOrDate, _reindex, _toDatetime, _BATCH_TYPES


def balanceSheet(symbol, token='', version=''):
    '''
    https://iexcloud.io/docs/api/#balance-sheet
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/balance-sheet', token, version)


def balanceSheetDF(symbol, token='', version=''):
    '''
    https://iexcloud.io/docs/api/#balance-sheet
    '''
    val = balanceSheet(symbol, token, version)
    df = pd.io.json.json_normalize(val, 'balancesheet', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    return df


def batch(symbols, types=None, _range='1m', last=10, token='', version=''):
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
        return _getJson(route, token, version)

    if len(symbols) > 100:
        raise PyEXception('IEX will only handle up to 100 symbols at a time!')
    route = 'stock/market/batch?symbols={}&types={}&range={}&last={}'.format(','.join(symbols), ','.join(types), _range, last)
    return _getJson(route, token, version)


def batchDF(symbols, types=None, _range='1m', last=10, token='', version=''):
    '''fetch a large number of fields at the same time'''
    x = batch(symbols, types, _range, last, token, version)

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


def bulkBatch(symbols, types=None, _range='1m', last=10, token='', version=''):
    '''fetch a large number of fields for multiple symbols all at the same time'''
    types = types or _BATCH_TYPES
    args = []
    empty_data = []
    list_orig = empty_data.__class__

    if not isinstance(symbols, list_orig):
        raise PyEXception('Symbols must be of type list')

    for i in range(0, len(symbols), 99):
        args.append((symbols[i:i+99], types, _range, last, token, version))

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


def bulkBatchDF(symbols, types=None, _range='1m', last=10, token='', version=''):
    '''fetch a large number of fields for multiple symbols all at the same time'''
    dat = bulkBatch(symbols, types, _range, last, token, version)
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


def book(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#book'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/book', token, version)


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


def bookDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#book'''
    x = book(symbol, token, version)
    df = _bookToDF(x)
    return df


def cashFlow(symbol, token='', version=''):
    '''
    https://iexcloud.io/docs/api/#cash-flow
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/cash-flow', token, version)


def cashFlowDF(symbol, token='', version=''):
    '''
    https://iexcloud.io/docs/api/#cash-flow
    '''
    val = cashFlow(symbol, token, version)
    df = pd.io.json.json_normalize(val, 'cashflow', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    return df


def chart(symbol, timeframe='1m', date=None, token='', version=''):
    '''
    https://iextrading.com/developer/docs/#chart
    https://iextrading.com/developer/docs/#time-series
    '''
    _raiseIfNotStr(symbol)
    if timeframe is not None and timeframe != '1d':
        if timeframe not in _TIMEFRAME_CHART:
            raise PyEXception('Range must be in %s' % str(_TIMEFRAME_CHART))
        return _getJson('stock/' + symbol + '/chart' + '/' + timeframe, token, version)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/' + symbol + '/chart' + '/date/' + date, token, version)
    return _getJson('stock/' + symbol + '/chart', token, version)


def _chartToDF(c):
    df = pd.DataFrame(c)
    _toDatetime(df)
    _reindex(df, 'date')
    return df


def chartDF(symbol, timeframe='1m', date=None, token='', version=''):
    '''
    https://iextrading.com/developer/docs/#chart
    https://iextrading.com/developer/docs/#time-series
    '''
    c = chart(symbol, timeframe, date, token, version)
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


def bulkMinuteBars(symbol, dates, token='', version=''):
    '''fetch many dates worth of minute-bars for a given symbol'''
    _raiseIfNotStr(symbol)
    dates = [_strOrDate(date) for date in dates]
    list_orig = dates.__class__

    args = []
    for date in dates:
        args.append((symbol, '1d', date, token, version))

    pool = ThreadPool(20)
    rets = pool.starmap(chart, args)
    pool.close()

    return list_orig(itertools.chain(*rets))


def bulkMinuteBarsDF(symbol, dates, token='', version=''):
    '''fetch many dates worth of minute-bars for a given symbol'''
    data = bulkMinuteBars(symbol, dates, token, version)
    df = pd.DataFrame(data)
    if df.empty:
        return df
    _toDatetime(df)
    df.set_index(['date', 'minute'], inplace=True)
    return df


def company(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#company'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/company', token, version)


def _companyToDF(c, token='', version=''):
    df = pd.io.json.json_normalize(c)
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def companyDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#company'''
    c = company(symbol, token, version)
    df = _companyToDF(c)
    return df


def collections(tag, collectionName, token='', version=''):
    '''https://iextrading.com/developer/docs/#collections'''
    if tag not in _COLLECTION_TAGS:
        raise PyEXception('Tag must be in %s' % str(_COLLECTION_TAGS))
    return _getJson('stock/market/collection/' + tag + '?collectionName=' + collectionName, token, version)


def collectionsDF(tag, query, token='', version=''):
    '''https://iextrading.com/developer/docs/#collections'''
    df = pd.DataFrame(collections(tag, query, token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def crypto(token='', version=''):
    '''https://iextrading.com/developer/docs/#collections'''
    return _getJson('stock/market/crypto/', token, version)


def cryptoDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#collections'''
    df = pd.DataFrame(crypto(token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def delayedQuote(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#delayed-quote'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/delayed-quote', token, version)


def delayedQuoteDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#delayed-quote'''
    df = pd.io.json.json_normalize(delayedQuote(symbol, token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def dividends(symbol, timeframe='ytd', token='', version=''):
    '''https://iextrading.com/developer/docs/#dividends'''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/dividends/' + timeframe, token, version)


def _dividendsToDF(d):
    df = pd.DataFrame(d)
    _toDatetime(df)
    _reindex(df, 'exDate')
    return df


def dividendsDF(symbol, timeframe='ytd', token='', version=''):
    '''https://iextrading.com/developer/docs/#dividends'''
    d = dividends(symbol, timeframe, token, version)
    df = _dividendsToDF(d)
    return df


def earnings(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#earnings'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/earnings', token, version)


def _earningsToDF(e):
    if e:
        df = pd.io.json.json_normalize(e, 'earnings', 'symbol')
        _toDatetime(df)
        _reindex(df, 'EPSReportDate')
    else:
        df = pd.DataFrame()
    return df


def earningsDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#earnings'''
    e = earnings(symbol, token, version)
    df = _earningsToDF(e)
    return df


def earningsToday(token='', version=''):
    '''https://iextrading.com/developer/docs/#earnings-today'''
    return _getJson('stock/market/today-earnings', token, version)


def earningsTodayDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#earnings-today'''
    x = earningsToday(token, version)
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


def spread(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#effective-spread'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/effective-spread', token, version)


def spreadDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#effective-spread'''
    df = pd.DataFrame(spread(symbol, token, version))
    _toDatetime(df)
    _reindex(df, 'venue')
    return df


def financials(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#financials'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/financials', token, version)


def _financialsToDF(f):
    if f:
        df = pd.io.json.json_normalize(f, 'financials', 'symbol')
        _toDatetime(df)
        _reindex(df, 'reportDate')
    else:
        df = pd.DataFrame()
    return df


def financialsDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#financials'''
    f = financials(symbol, token, version)
    df = _financialsToDF(f)
    return df


def incomeStatement(symbol, token='', version=''):
    '''
    https://iexcloud.io/docs/api/#income-statement
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/income', token, version)


def incomeStatementDF(symbol, token='', version=''):
    '''
    https://iexcloud.io/docs/api/#income-statement
    '''
    val = incomeStatement(symbol, token, version)
    df = pd.io.json.json_normalize(val, 'income', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    return df


def ipoToday(token='', version=''):
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    return _getJson('stock/market/today-ipos', token, version)


def ipoTodayDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    val = ipoToday(token, version)
    if val:
        df = pd.io.json.json_normalize(val, 'rawData')
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def ipoUpcoming(token='', version=''):
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    return _getJson('stock/market/upcoming-ipos', token, version)


def ipoUpcomingDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#ipo-calendar'''
    val = ipoUpcoming(token, version)
    if val:
        df = pd.io.json.json_normalize(val, 'rawData')
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def threshold(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list'''
    if date:
        date = _strOrDate(date)
        return _getJson('stock/market/threshold-securities/' + date, token, version)
    return _getJson('stock/market/threshold-securities', token, version)


def thresholdDF(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-regulation-sho-threshold-securities-list'''
    df = pd.DataFrame(threshold(date, token, version))
    _toDatetime(df)
    return df


def shortInterest(symbol, date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    _raiseIfNotStr(symbol)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/' + symbol + '/short-interest/' + date, token, version)
    return _getJson('stock/' + symbol + '/short-interest', token, version)


def shortInterestDF(symbol, date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    df = pd.DataFrame(shortInterest(symbol, date, token, version))
    _toDatetime(df)
    return df


def marketShortInterest(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    if date:
        date = _strOrDate(date)
        return _getJson('stock/market/short-interest/' + date, token, version)
    return _getJson('stock/market/short-interest', token, version)


def marketShortInterestDF(date=None, token='', version=''):
    '''https://iextrading.com/developer/docs/#iex-short-interest-list'''
    df = pd.DataFrame(marketShortInterest(date, token, version))
    _toDatetime(df)
    return df


def stockStats(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#key-stats'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/stats', token, version)


def _statsToDF(s):
    if s:
        df = pd.io.json.json_normalize(s)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def stockStatsDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#key-stats'''
    s = stockStats(symbol, token, version)
    df = _statsToDF(s)
    return df


def largestTrades(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#largest-trades'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/largest-trades', token, version)


def largestTradesDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#largest-trades'''
    df = pd.DataFrame(largestTrades(symbol, token, version))
    _toDatetime(df)
    _reindex(df, 'time')
    return df


def list(option='mostactive', token='', version=''):
    '''https://iextrading.com/developer/docs/#list'''
    if option not in _LIST_OPTIONS:
        raise PyEXception('Option must be in %s' % str(_LIST_OPTIONS))
    return _getJson('stock/market/list/' + option, token, version)


def listDF(option='mostactive', token='', version=''):
    '''https://iextrading.com/developer/docs/#list'''
    df = pd.DataFrame(list(option, token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def logo(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#logo'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/logo', token, version)


def logoPNG(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#logo'''
    _raiseIfNotStr(symbol)
    response = requests.get(logo(symbol, token, version)['url'])
    return ImageP.open(BytesIO(response.content))


def logoNotebook(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#logo'''
    _raiseIfNotStr(symbol)
    url = logo(symbol, token, version)['url']
    return ImageI(url=url)


def news(symbol, count=10, token='', version=''):
    '''https://iextrading.com/developer/docs/#news'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/news/last/' + str(count), token, version)


def _newsToDF(n):
    df = pd.DataFrame(n)
    _toDatetime(df)
    _reindex(df, 'datetime')
    return df


def newsDF(symbol, count=10, token='', version=''):
    '''https://iextrading.com/developer/docs/#news'''
    n = news(symbol, count, token, version)
    df = _newsToDF(n)
    return df


def marketNews(count=10, token='', version=''):
    '''https://iextrading.com/developer/docs/#news'''
    return _getJson('stock/market/news/last/' + str(count), token, version)


def marketNewsDF(count=10, token='', version=''):
    '''https://iextrading.com/developer/docs/#news'''
    df = pd.DataFrame(marketNews(count, token, version))
    _toDatetime(df)
    _reindex(df, 'datetime')
    return df


def ohlc(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#ohlc'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/ohlc', token, version)


def ohlcDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#ohlc'''
    o = ohlc(symbol, token, version)
    if o:
        df = pd.io.json.json_normalize(o)
        _toDatetime(df)
    else:
        df = pd.DataFrame()
    return df


def marketOhlc(token='', version=''):
    '''https://iextrading.com/developer/docs/#ohlc'''
    return _getJson('stock/market/ohlc', token, version)


def marketOhlcDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#ohlc'''
    x = marketOhlc(token, version)
    data = []
    for key in x:
        data.append(x[key])
        data[-1]['symbol'] = key
    df = pd.io.json.json_normalize(data)
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def peers(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#peers'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/peers', token, version)


def _peersToDF(p):
    df = pd.DataFrame(p, columns=['symbol'])
    _toDatetime(df)
    _reindex(df, 'symbol')
    df['peer'] = df.index
    return df


def peersDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#peers'''
    p = peers(symbol, token, version)
    df = _peersToDF(p)
    return df


def yesterday(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#previous'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/previous', token, version)


def yesterdayDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#previous'''
    y = yesterday(symbol, token, version)
    if y:
        df = pd.io.json.json_normalize(y)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def marketYesterday(token='', version=''):
    '''https://iextrading.com/developer/docs/#previous'''
    return _getJson('stock/market/previous', token, version)


def marketYesterdayDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#previous'''
    x = marketYesterday(token, version)
    data = []
    for key in x:
        data.append(x[key])
        data[-1]['symbol'] = key
    df = pd.DataFrame(data)
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def price(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#price'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/price', token, version)


def priceDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#price'''
    df = pd.io.json.json_normalize({'price': price(symbol, token, version)})
    _toDatetime(df)
    return df


def quote(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#quote'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/quote', token, version)


def quoteDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#quote'''
    q = quote(symbol, token, version)
    if q:
        df = pd.io.json.json_normalize(q)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def relevant(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#relevant'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/relevant', token, version)


def relevantDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#relevant'''
    df = pd.DataFrame(relevant(symbol, token, version))
    _toDatetime(df)
    return df


def sectorPerformance(token='', version=''):
    '''https://iextrading.com/developer/docs/#sector-performance'''
    return _getJson('stock/market/sector-performance', token, version)


def sectorPerformanceDF(token='', version=''):
    '''https://iextrading.com/developer/docs/#sector-performance'''
    df = pd.DataFrame(sectorPerformance(token, version))
    _toDatetime(df)
    _reindex(df, 'name')
    return df


def splits(symbol, timeframe='ytd', token='', version=''):
    '''https://iextrading.com/developer/docs/#splits'''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/splits/' + timeframe, token, version)


def _splitsToDF(s):
    df = pd.DataFrame(s)
    _toDatetime(df)
    _reindex(df, 'exDate')
    return df


def splitsDF(symbol, timeframe='ytd', token='', version=''):
    '''https://iextrading.com/developer/docs/#splits'''
    s = splits(symbol, timeframe, token, version)
    df = _splitsToDF(s)
    return df


def volumeByVenue(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#volume-by-venue'''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/volume-by-venue', token, version)


def volumeByVenueDF(symbol, token='', version=''):
    '''https://iextrading.com/developer/docs/#volume-by-venue'''
    df = pd.DataFrame(volumeByVenue(symbol, token, version))
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

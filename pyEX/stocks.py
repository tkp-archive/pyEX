import itertools
import requests
import pandas as pd
import numpy as np
from io import BytesIO
from IPython.display import Image as ImageI
from multiprocessing.pool import ThreadPool
from PIL import Image as ImageP
from .common import _TIMEFRAME_CHART, _TIMEFRAME_DIVSPLIT, _LIST_OPTIONS, _COLLECTION_TAGS, _getJson, _raiseIfNotStr, PyEXception, _strOrDate, _reindex, _toDatetime, _BATCH_TYPES


def balanceSheet(symbol, token='', version=''):
    '''Pulls balance sheet data. Available quarterly (4 quarters) and annually (4 years)

    https://iexcloud.io/docs/api/#balance-sheet
    Updates at 8am, 9am UTC daily


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/balance-sheet', token, version)


def balanceSheetDF(symbol, token='', version=''):
    '''Pulls balance sheet data. Available quarterly (4 quarters) and annually (4 years)

    https://iexcloud.io/docs/api/#balance-sheet
    Updates at 8am, 9am UTC daily


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    val = balanceSheet(symbol, token, version)
    df = pd.io.json.json_normalize(val, 'balancesheet', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    return df


def batch(symbols, fields=None, range_='1m', last=10, token='', version=''):
    '''Batch several data requests into one invocation

    https://iexcloud.io/docs/api/#batch-requests


    Args:
        symbols (list); List of tickers to request
        fields (list); List of fields to request
        range_ (string); Date range for chart
        last (int);
        token (string); Access token
        version (string); API version

    Returns:
        dict: results in json
    '''
    fields = fields or _BATCH_TYPES[:10]  # limit 10

    if not isinstance(symbols, [].__class__):
        if not isinstance(symbols, str):
            raise PyEXception('batch expects string or list of strings for symbols argument')

    if isinstance(fields, str):
        fields = [fields]

    if range_ not in _TIMEFRAME_CHART:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_CHART))

    if isinstance(symbols, str):
        route = 'stock/{}/batch?types={}&range={}&last={}'.format(symbols, ','.join(fields), range_, last)
        return _getJson(route, token, version)

    if len(symbols) > 100:
        raise PyEXception('IEX will only handle up to 100 symbols at a time!')
    route = 'stock/market/batch?symbols={}&types={}&range={}&last={}'.format(','.join(symbols), ','.join(fields), range_, last)
    return _getJson(route, token, version)


def batchDF(symbols, fields=None, range_='1m', last=10, token='', version=''):
    '''Batch several data requests into one invocation

    https://iexcloud.io/docs/api/#batch-requests


    Args:
        symbols (list); List of tickers to request
        fields (list); List of fields to request
        range_ (string); Date range for chart
        last (int);
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: results in json
    '''
    x = batch(symbols, fields, range_, last, token, version)

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
                dat['symbol'] = symbol

                ret[field] = pd.concat([ret[field], dat], sort=True)
    return ret


def bulkBatch(symbols, fields=None, range_='1m', last=10, token='', version=''):
    '''Optimized batch to fetch as much as possible at once

    https://iexcloud.io/docs/api/#batch-requests


    Args:
        symbols (list); List of tickers to request
        fields (list); List of fields to request
        range_ (string); Date range for chart
        last (int);
        token (string); Access token
        version (string); API version

    Returns:
        dict: results in json
    '''
    fields = fields or _BATCH_TYPES
    args = []
    empty_data = []
    list_orig = empty_data.__class__

    if not isinstance(symbols, list_orig):
        raise PyEXception('Symbols must be of type list')

    for i in range(0, len(symbols), 99):
        args.append((symbols[i:i+99], fields, range_, last, token, version))

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
            if isinstance(fields, str):
                ret[k] = {}
            else:
                ret[k] = {x: {} for x in fields}
    return ret


def bulkBatchDF(symbols, fields=None, range_='1m', last=10, token='', version=''):
    '''Optimized batch to fetch as much as possible at once

    https://iexcloud.io/docs/api/#batch-requests


    Args:
        symbols (list); List of tickers to request
        fields (list); List of fields to request
        range_ (string); Date range for chart
        last (int);
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: results in json
    '''
    dat = bulkBatch(symbols, fields, range_, last, token, version)
    ret = {}
    for symbol in dat:
        for field in dat[symbol]:
            if field not in ret:
                ret[field] = pd.DataFrame()

            d = dat[symbol][field]
            d = _MAPPING[field](d)
            d['symbol'] = symbol
            ret[field] = pd.concat([ret[field], d], sort=True)

    return ret


def book(symbol, token='', version=''):
    '''Book data

    https://iextrading.com/developer/docs/#book
    realtime during Investors Exchange market hours

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/book', token, version)


def _bookToDF(b):
    '''internal'''
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
    '''Book data

    https://iextrading.com/developer/docs/#book
    realtime during Investors Exchange market hours

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    x = book(symbol, token, version)
    df = _bookToDF(x)
    return df


def cashFlow(symbol, token='', version=''):
    '''Pulls cash flow data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#cash-flow
    Updates at 8am, 9am UTC daily


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/cash-flow', token, version)


def cashFlowDF(symbol, token='', version=''):
    '''Pulls cash flow data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#cash-flow
    Updates at 8am, 9am UTC daily


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    val = cashFlow(symbol, token, version)
    df = pd.io.json.json_normalize(val, 'cashflow', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    df.replace(to_replace=[None], value=np.nan, inplace=True)
    return df


def chart(symbol, timeframe='1m', date=None, token='', version=''):
    '''Historical price/volume data, daily and intraday

    https://iexcloud.io/docs/api/#historical-prices
    Data Schedule
    1d: -9:30-4pm ET Mon-Fri on regular market trading days
        -9:30-1pm ET on early close trading days
    All others:
        -Prior trading day available after 4am ET Tue-Sat

    Args:
        symbol (string); Ticker to request
        timeframe (string); Timeframe to request e.g. 1m
        date (datetime): date, if requesting intraday
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
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
    '''internal'''
    df = pd.DataFrame(c)
    _toDatetime(df)
    _reindex(df, 'date')
    return df


def chartDF(symbol, timeframe='1m', date=None, token='', version=''):
    '''Historical price/volume data, daily and intraday

    https://iexcloud.io/docs/api/#historical-prices
    Data Schedule
    1d: -9:30-4pm ET Mon-Fri on regular market trading days
        -9:30-1pm ET on early close trading days
    All others:
        -Prior trading day available after 4am ET Tue-Sat

    Args:
        symbol (string); Ticker to request
        timeframe (string); Timeframe to request e.g. 1m
        date (datetime): date, if requesting intraday
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
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


def collections(tag, collectionName, token='', version=''):
    '''Returns an array of quote objects for a given collection type. Currently supported collection types are sector, tag, and list


    https://iexcloud.io/docs/api/#collections

    Args:
        tag (string);  Sector, Tag, or List
        collectionName (string);  Associated name for tag
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    if tag not in _COLLECTION_TAGS:
        raise PyEXception('Tag must be in %s' % str(_COLLECTION_TAGS))
    return _getJson('stock/market/collection/' + tag + '?collectionName=' + collectionName, token, version)


def collectionsDF(tag, query, token='', version=''):
    '''Returns an array of quote objects for a given collection type. Currently supported collection types are sector, tag, and list


    https://iexcloud.io/docs/api/#collections

    Args:
        tag (string);  Sector, Tag, or List
        collectionName (string);  Associated name for tag
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(collections(tag, query, token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def company(symbol, token='', version=''):
    '''Company reference data

    https://iexcloud.io/docs/api/#company
    Updates at 4am and 5am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/company', token, version)


def _companyToDF(c, token='', version=''):
    '''internal'''
    df = pd.io.json.json_normalize(c)
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def companyDF(symbol, token='', version=''):
    '''Company reference data

    https://iexcloud.io/docs/api/#company
    Updates at 4am and 5am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    c = company(symbol, token, version)
    df = _companyToDF(c)
    return df


def delayedQuote(symbol, token='', version=''):
    '''This returns the 15 minute delayed market quote.

    https://iexcloud.io/docs/api/#delayed-quote
    15min delayed
    4:30am - 8pm ET M-F when market is open

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/delayed-quote', token, version)


def delayedQuoteDF(symbol, token='', version=''):
    '''This returns the 15 minute delayed market quote.

    https://iexcloud.io/docs/api/#delayed-quote
    15min delayed
    4:30am - 8pm ET M-F when market is open

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(delayedQuote(symbol, token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def dividends(symbol, timeframe='ytd', token='', version=''):
    '''Dividend history

    https://iexcloud.io/docs/api/#dividends
    Updated at 9am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/dividends/' + timeframe, token, version)


def _dividendsToDF(d):
    '''internal'''
    df = pd.DataFrame(d)
    _toDatetime(df)
    _reindex(df, 'exDate')
    return df


def dividendsDF(symbol, timeframe='ytd', token='', version=''):
    '''Dividend history

    https://iexcloud.io/docs/api/#dividends
    Updated at 9am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    d = dividends(symbol, timeframe, token, version)
    df = _dividendsToDF(d)
    return df


def earnings(symbol, token='', version=''):
    '''Earnings data for a given company including the actual EPS, consensus, and fiscal period. Earnings are available quarterly (last 4 quarters) and annually (last 4 years).

    https://iexcloud.io/docs/api/#earnings
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/earnings', token, version)


def _earningsToDF(e):
    '''internal'''
    if e:
        df = pd.io.json.json_normalize(e, 'earnings', 'symbol')
        _toDatetime(df)
        _reindex(df, 'EPSReportDate')
    else:
        df = pd.DataFrame()
    return df


def earningsDF(symbol, token='', version=''):
    '''Earnings data for a given company including the actual EPS, consensus, and fiscal period. Earnings are available quarterly (last 4 quarters) and annually (last 4 years).

    https://iexcloud.io/docs/api/#earnings
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    e = earnings(symbol, token, version)
    df = _earningsToDF(e)
    return df


def earningsToday(token='', version=''):
    '''Returns earnings that will be reported today as two arrays: before the open bto and after market close amc.
    Each array contains an object with all keys from earnings, a quote object, and a headline key.

    https://iexcloud.io/docs/api/#earnings-today
    Updates at 9am, 11am, 12pm UTC daily


    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('stock/market/today-earnings', token, version)


def earningsTodayDF(token='', version=''):
    '''Returns earnings that will be reported today as two arrays: before the open bto and after market close amc.
    Each array contains an object with all keys from earnings, a quote object, and a headline key.

    https://iexcloud.io/docs/api/#earnings-today
    Updates at 9am, 11am, 12pm UTC daily


    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
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
    '''This returns an array of effective spread, eligible volume, and price improvement of a stock, by market.
    Unlike volume-by-venue, this will only return a venue if effective spread is not ‘N/A’. Values are sorted in descending order by effectiveSpread.
    Lower effectiveSpread and higher priceImprovement values are generally considered optimal.

    Effective spread is designed to measure marketable orders executed in relation to the market center’s
    quoted spread and takes into account hidden and midpoint liquidity available at each market center.
    Effective Spread is calculated by using eligible trade prices recorded to the consolidated tape and
    comparing those trade prices to the National Best Bid and Offer (“NBBO”) at the time of the execution.

    View the data disclaimer at the bottom of the stocks app for more information about how these values are calculated.


    https://iexcloud.io/docs/api/#earnings-today
    8am ET M-F

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/effective-spread', token, version)


def spreadDF(symbol, token='', version=''):
    '''This returns an array of effective spread, eligible volume, and price improvement of a stock, by market.
    Unlike volume-by-venue, this will only return a venue if effective spread is not ‘N/A’. Values are sorted in descending order by effectiveSpread.
    Lower effectiveSpread and higher priceImprovement values are generally considered optimal.

    Effective spread is designed to measure marketable orders executed in relation to the market center’s
    quoted spread and takes into account hidden and midpoint liquidity available at each market center.
    Effective Spread is calculated by using eligible trade prices recorded to the consolidated tape and
    comparing those trade prices to the National Best Bid and Offer (“NBBO”) at the time of the execution.

    View the data disclaimer at the bottom of the stocks app for more information about how these values are calculated.


    https://iexcloud.io/docs/api/#earnings-today
    8am ET M-F

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(spread(symbol, token, version))
    _toDatetime(df)
    _reindex(df, 'venue')
    return df


def estimates(symbol, token='', version=''):
    '''Provides the latest consensus estimate for the next fiscal period

    https://iexcloud.io/docs/api/#estimates
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/estimates', token, version)


def _estimatesToDF(f):
    '''internal'''
    if f:
        df = pd.io.json.json_normalize(f, 'estimates', 'symbol')
        _toDatetime(df)
        _reindex(df, 'fiscalEndDate')
    else:
        df = pd.DataFrame()
    return df


def estimatesDF(symbol, token='', version=''):
    '''Provides the latest consensus estimate for the next fiscal period

    https://iexcloud.io/docs/api/#estimates
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    f = estimates(symbol, token, version)
    df = _estimatesToDF(f)
    return df


def financials(symbol, token='', version=''):
    '''Pulls income statement, balance sheet, and cash flow data from the four most recent reported quarters.

    https://iexcloud.io/docs/api/#financials
    Updates at 8am, 9am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/financials', token, version)


def _financialsToDF(f):
    '''internal'''
    if f:
        df = pd.io.json.json_normalize(f, 'financials', 'symbol')
        _toDatetime(df)
        _reindex(df, 'reportDate')
    else:
        df = pd.DataFrame()
    return df


def financialsDF(symbol, token='', version=''):
    '''Pulls income statement, balance sheet, and cash flow data from the four most recent reported quarters.

    https://iexcloud.io/docs/api/#financials
    Updates at 8am, 9am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    f = financials(symbol, token, version)
    df = _financialsToDF(f)
    return df


def incomeStatement(symbol, token='', version=''):
    '''Pulls income statement data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#income-statement
    Updates at 8am, 9am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/income', token, version)


def incomeStatementDF(symbol, token='', version=''):
    '''Pulls income statement data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#income-statement
    Updates at 8am, 9am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    val = incomeStatement(symbol, token, version)
    df = pd.io.json.json_normalize(val, 'income', 'symbol')
    _toDatetime(df)
    _reindex(df, 'reportDate')
    return df


def ipoToday(token='', version=''):
    '''This returns a list of upcoming or today IPOs scheduled for the current and next month. The response is split into two structures:
    rawData and viewData. rawData represents all available data for an IPO. viewData represents data structured for display to a user.

    https://iexcloud.io/docs/api/#ipo-calendar
    10am, 10:30am UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('stock/market/today-ipos', token, version)


def ipoTodayDF(token='', version=''):
    '''This returns a list of upcoming or today IPOs scheduled for the current and next month. The response is split into two structures:
    rawData and viewData. rawData represents all available data for an IPO. viewData represents data structured for display to a user.

    https://iexcloud.io/docs/api/#ipo-calendar
    10am, 10:30am UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    val = ipoToday(token, version)
    if val:
        df = pd.io.json.json_normalize(val, 'rawData')
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def ipoUpcoming(token='', version=''):
    '''This returns a list of upcoming or today IPOs scheduled for the current and next month. The response is split into two structures:
    rawData and viewData. rawData represents all available data for an IPO. viewData represents data structured for display to a user.

    https://iexcloud.io/docs/api/#ipo-calendar
    10am, 10:30am UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('stock/market/upcoming-ipos', token, version)


def ipoUpcomingDF(token='', version=''):
    '''This returns a list of upcoming or today IPOs scheduled for the current and next month. The response is split into two structures:
    rawData and viewData. rawData represents all available data for an IPO. viewData represents data structured for display to a user.

    https://iexcloud.io/docs/api/#ipo-calendar
    10am, 10:30am UTC daily

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    val = ipoUpcoming(token, version)
    if val:
        df = pd.io.json.json_normalize(val, 'rawData')
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def keyStats(symbol, token='', version=''):
    '''Key Stats about company

    https://iexcloud.io/docs/api/#key-stats
    8am, 9am ET

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/stats', token, version)


def _statsToDF(s):
    '''internal'''
    if s:
        df = pd.io.json.json_normalize(s)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def keyStatsDF(symbol, token='', version=''):
    '''Key Stats about company

    https://iexcloud.io/docs/api/#key-stats
    8am, 9am ET

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    s = keyStats(symbol, token, version)
    df = _statsToDF(s)
    return df


def largestTrades(symbol, token='', version=''):
    '''This returns 15 minute delayed, last sale eligible trades.

    https://iexcloud.io/docs/api/#largest-trades
    9:30-4pm ET M-F during regular market hours

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/largest-trades', token, version)


def largestTradesDF(symbol, token='', version=''):
    '''This returns 15 minute delayed, last sale eligible trades.

    https://iexcloud.io/docs/api/#largest-trades
    9:30-4pm ET M-F during regular market hours

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(largestTrades(symbol, token, version))
    _toDatetime(df)
    _reindex(df, 'time')
    return df


def list(option='mostactive', token='', version=''):
    '''Returns an array of quotes for the top 10 symbols in a specified list.


    https://iexcloud.io/docs/api/#list
    Updated intraday

    Args:
        option (string); Option to query
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    if option not in _LIST_OPTIONS:
        raise PyEXception('Option must be in %s' % str(_LIST_OPTIONS))
    return _getJson('stock/market/list/' + option, token, version)


def listDF(option='mostactive', token='', version=''):
    '''Returns an array of quotes for the top 10 symbols in a specified list.


    https://iexcloud.io/docs/api/#list
    Updated intraday

    Args:
        option (string); Option to query
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(list(option, token, version))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def logo(symbol, token='', version=''):
    '''This is a helper function, but the google APIs url is standardized.

    https://iexcloud.io/docs/api/#logo
    8am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/logo', token, version)


def logoPNG(symbol, token='', version=''):
    '''This is a helper function, but the google APIs url is standardized.

    https://iexcloud.io/docs/api/#logo
    8am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        image: result as png
    '''
    _raiseIfNotStr(symbol)
    response = requests.get(logo(symbol, token, version)['url'])
    return ImageP.open(BytesIO(response.content))


def logoNotebook(symbol, token='', version=''):
    '''This is a helper function, but the google APIs url is standardized.

    https://iexcloud.io/docs/api/#logo
    8am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        image: result
    '''
    _raiseIfNotStr(symbol)
    url = logo(symbol, token, version)['url']
    return ImageI(url=url)


def marketVolume(token='', version=''):
    '''This endpoint returns real time traded volume on U.S. markets.

    https://iexcloud.io/docs/api/#market-volume-u-s
    7:45am-5:15pm ET Mon-Fri

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('market/', token, version)


def marketVolumeDF(token='', version=''):
    '''This endpoint returns real time traded volume on U.S. markets.

    https://iexcloud.io/docs/api/#market-volume-u-s
    7:45am-5:15pm ET Mon-Fri

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(marketVolume())


def news(symbol, count=10, token='', version=''):
    '''News about company

    https://iexcloud.io/docs/api/#news
    Continuous

    Args:
        symbol (string); Ticker to request
        count (int): limit number of results
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/news/last/' + str(count), token, version)


def _newsToDF(n):
    '''internal'''
    df = pd.DataFrame(n)
    _toDatetime(df)
    _reindex(df, 'datetime')
    return df


def newsDF(symbol, count=10, token='', version=''):
    '''News about company

    https://iexcloud.io/docs/api/#news
    Continuous

    Args:
        symbol (string); Ticker to request
        count (int): limit number of results
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    n = news(symbol, count, token, version)
    df = _newsToDF(n)
    return df


def marketNews(count=10, token='', version=''):
    '''News about market

    https://iexcloud.io/docs/api/#news
    Continuous

    Args:
        count (int): limit number of results
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('stock/market/news/last/' + str(count), token, version)


def marketNewsDF(count=10, token='', version=''):
    '''News about market

    https://iexcloud.io/docs/api/#news
    Continuous

    Args:
        count (int): limit number of results
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(marketNews(count, token, version))
    _toDatetime(df)
    _reindex(df, 'datetime')
    return df


def ohlc(symbol, token='', version=''):
    '''Returns the official open and close for a give symbol.

    https://iexcloud.io/docs/api/#news
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/ohlc', token, version)


def ohlcDF(symbol, token='', version=''):
    '''Returns the official open and close for a give symbol.

    https://iexcloud.io/docs/api/#news
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    o = ohlc(symbol, token, version)
    if o:
        df = pd.io.json.json_normalize(o)
        _toDatetime(df)
    else:
        df = pd.DataFrame()
    return df


def marketOhlc(token='', version=''):
    '''Returns the official open and close for whole market.

    https://iexcloud.io/docs/api/#news
    9:30am-5pm ET Mon-Fri

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('stock/market/ohlc', token, version)


def marketOhlcDF(token='', version=''):
    '''Returns the official open and close for whole market.

    https://iexcloud.io/docs/api/#news
    9:30am-5pm ET Mon-Fri

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
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
    '''Peers of ticker

    https://iexcloud.io/docs/api/#peers
    8am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/peers', token, version)


def _peersToDF(p):
    '''internal'''
    df = pd.DataFrame(p, columns=['symbol'])
    _toDatetime(df)
    _reindex(df, 'symbol')
    df['peer'] = df.index
    return df


def peersDF(symbol, token='', version=''):
    '''Peers of ticker

    https://iexcloud.io/docs/api/#peers
    8am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    p = peers(symbol, token, version)
    df = _peersToDF(p)
    return df


def yesterday(symbol, token='', version=''):
    '''This returns previous day adjusted price data for one or more stocks

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/previous', token, version)


def yesterdayDF(symbol, token='', version=''):
    '''This returns previous day adjusted price data for one or more stocks

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    y = yesterday(symbol, token, version)
    if y:
        df = pd.io.json.json_normalize(y)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def marketYesterday(token='', version=''):
    '''This returns previous day adjusted price data for whole market

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('stock/market/previous', token, version)


def marketYesterdayDF(token='', version=''):
    '''This returns previous day adjusted price data for whole market

    https://iexcloud.io/docs/api/#previous-day-prices
    Available after 4am ET Tue-Sat

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
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
    '''Price of ticker

    https://iexcloud.io/docs/api/#price
    4:30am-8pm ET Mon-Fri

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/price', token, version)


def priceDF(symbol, token='', version=''):
    '''Price of ticker

    https://iexcloud.io/docs/api/#price
    4:30am-8pm ET Mon-Fri

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize({'price': price(symbol, token, version)})
    _toDatetime(df)
    return df


def priceTarget(symbol, token='', version=''):
    '''Provides the latest avg, high, and low analyst price target for a symbol.

    https://iexcloud.io/docs/api/#price-target
    Updates at 10am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/price-target', token, version)


def priceTargetDF(symbol, token='', version=''):
    '''Provides the latest avg, high, and low analyst price target for a symbol.

    https://iexcloud.io/docs/api/#price-target
    Updates at 10am, 11am, 12pm UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.io.json.json_normalize(priceTarget(symbol, token, version))
    _toDatetime(df)
    return df


def quote(symbol, token='', version=''):
    '''Get quote for ticker

    https://iexcloud.io/docs/api/#quote
    4:30am-8pm ET Mon-Fri


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/quote', token, version)


def quoteDF(symbol, token='', version=''):
    '''Get quote for ticker

    https://iexcloud.io/docs/api/#quote
    4:30am-8pm ET Mon-Fri


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    q = quote(symbol, token, version)
    if q:
        df = pd.io.json.json_normalize(q)
        _toDatetime(df)
        _reindex(df, 'symbol')
    else:
        df = pd.DataFrame()
    return df


def relevant(symbol, token='', version=''):
    '''Same as peers

    https://iexcloud.io/docs/api/#relevant
    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/relevant', token, version)


def relevantDF(symbol, token='', version=''):
    '''Same as peers

    https://iexcloud.io/docs/api/#relevant
    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(relevant(symbol, token, version))
    _toDatetime(df)
    return df


def sectorPerformance(token='', version=''):
    '''This returns an array of each sector and performance for the current trading day. Performance is based on each sector ETF.

    https://iexcloud.io/docs/api/#sector-performance
    8am-5pm ET Mon-Fri

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    return _getJson('stock/market/sector-performance', token, version)


def sectorPerformanceDF(token='', version=''):
    '''This returns an array of each sector and performance for the current trading day. Performance is based on each sector ETF.

    https://iexcloud.io/docs/api/#sector-performance
    8am-5pm ET Mon-Fri

    Args:
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(sectorPerformance(token, version))
    _toDatetime(df)
    _reindex(df, 'name')
    return df


def splits(symbol, timeframe='ytd', token='', version=''):
    '''Stock split history

    https://iexcloud.io/docs/api/#splits
    Updated at 9am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception('Range must be in %s' % str(_TIMEFRAME_DIVSPLIT))
    return _getJson('stock/' + symbol + '/splits/' + timeframe, token, version)


def _splitsToDF(s):
    '''internal'''
    df = pd.DataFrame(s)
    _toDatetime(df)
    _reindex(df, 'exDate')
    return df


def splitsDF(symbol, timeframe='ytd', token='', version=''):
    '''Stock split history

    https://iexcloud.io/docs/api/#splits
    Updated at 9am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    s = splits(symbol, timeframe, token, version)
    df = _splitsToDF(s)
    return df


def volumeByVenue(symbol, token='', version=''):
    '''This returns 15 minute delayed and 30 day average consolidated volume percentage of a stock, by market.
    This call will always return 13 values, and will be sorted in ascending order by current day trading volume percentage.

    https://iexcloud.io/docs/api/#volume-by-venue
    Updated during regular market hours 9:30am-4pm ET


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/volume-by-venue', token, version)


def volumeByVenueDF(symbol, token='', version=''):
    '''This returns 15 minute delayed and 30 day average consolidated volume percentage of a stock, by market.
    This call will always return 13 values, and will be sorted in ascending order by current day trading volume percentage.

    https://iexcloud.io/docs/api/#volume-by-venue
    Updated during regular market hours 9:30am-4pm ET


    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(volumeByVenue(symbol, token, version))
    _toDatetime(df)
    _reindex(df, 'venue')
    return df


def threshold(date=None, token='', version=''):
    '''The following are IEX-listed securities that have an aggregate fail to deliver position for five consecutive settlement days at a registered clearing agency, totaling 10,000 shares or more and equal to at least 0.5% of the issuer’s total shares outstanding (i.e., “threshold securities”).
    The report data will be published to the IEX website daily at 8:30 p.m. ET with data for that trading day.

    https://iexcloud.io/docs/api/#listed-regulation-sho-threshold-securities-list-in-dev

    Args:
        date (datetime); Effective Datetime
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('stock/market/threshold-securities/' + date, token, version)
    return _getJson('stock/market/threshold-securities', token, version)


def thresholdDF(date=None, token='', version=''):
    '''The following are IEX-listed securities that have an aggregate fail to deliver position for five consecutive settlement days at a registered clearing agency, totaling 10,000 shares or more and equal to at least 0.5% of the issuer’s total shares outstanding (i.e., “threshold securities”).
    The report data will be published to the IEX website daily at 8:30 p.m. ET with data for that trading day.

    https://iexcloud.io/docs/api/#listed-regulation-sho-threshold-securities-list-in-dev

    Args:
        date (datetime); Effective Datetime
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(threshold(date, token, version))
    _toDatetime(df)
    return df


def shortInterest(symbol, date=None, token='', version=''):
    '''The consolidated market short interest positions in all IEX-listed securities are included in the IEX Short Interest Report.

    The report data will be published daily at 4:00pm ET.

    https://iexcloud.io/docs/api/#listed-short-interest-list-in-dev

    Args:
        symbol (string); Ticker to request
        date (datetime); Effective Datetime
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    if date:
        date = _strOrDate(date)
        return _getJson('stock/' + symbol + '/short-interest/' + date, token, version)
    return _getJson('stock/' + symbol + '/short-interest', token, version)


def shortInterestDF(symbol, date=None, token='', version=''):
    '''The consolidated market short interest positions in all IEX-listed securities are included in the IEX Short Interest Report.

    The report data will be published daily at 4:00pm ET.

    https://iexcloud.io/docs/api/#listed-short-interest-list-in-dev

    Args:
        symbol (string); Ticker to request
        date (datetime); Effective Datetime
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(shortInterest(symbol, date, token, version))
    _toDatetime(df)
    return df


def marketShortInterest(date=None, token='', version=''):
    '''The consolidated market short interest positions in all IEX-listed securities are included in the IEX Short Interest Report.

    The report data will be published daily at 4:00pm ET.

    https://iexcloud.io/docs/api/#listed-short-interest-list-in-dev

    Args:
        date (datetime); Effective Datetime
        token (string); Access token
        version (string); API version

    Returns:
        dict: result
    '''
    if date:
        date = _strOrDate(date)
        return _getJson('stock/market/short-interest/' + date, token, version)
    return _getJson('stock/market/short-interest', token, version)


def marketShortInterestDF(date=None, token='', version=''):
    '''The consolidated market short interest positions in all IEX-listed securities are included in the IEX Short Interest Report.

    The report data will be published daily at 4:00pm ET.

    https://iexcloud.io/docs/api/#listed-short-interest-list-in-dev

    Args:
        date (datetime); Effective Datetime
        token (string); Access token
        version (string); API version

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(marketShortInterest(date, token, version))
    _toDatetime(df)
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
    'splits': _splitsToDF
}

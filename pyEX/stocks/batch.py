# -*- coding: utf-8 -*-
import itertools
import pandas as pd
from multiprocessing.pool import ThreadPool
from ..common import _TIMEFRAME_CHART, _getJson, _raiseIfNotStr, PyEXception, _strOrDate, _toDatetime, _BATCH_TYPES
from .fundamentals import _dividendsToDF, _earningsToDF, _financialsToDF, _splitsToDF
from .news import _newsToDF
from .prices import chart, _bookToDF, _chartToDF
from .profiles import _companyToDF, _peersToDF
from .research import _statsToDF


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


def batch(symbols, fields=None, range_='1m', last=10, token='', version='', filter=''):
    '''Batch several data requests into one invocation

    https://iexcloud.io/docs/api/#batch-requests


    Args:
        symbols (list); List of tickers to request
        fields (list); List of fields to request
        range_ (string); Date range for chart
        last (int);
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

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
        return _getJson(route, token, version, filter)

    if len(symbols) > 100:
        raise PyEXception('IEX will only handle up to 100 symbols at a time!')
    route = 'stock/market/batch?symbols={}&types={}&range={}&last={}'.format(','.join(symbols), ','.join(fields), range_, last)
    return _getJson(route, token, version, filter)


def batchDF(symbols, fields=None, range_='1m', last=10, token='', version='', filter=''):
    '''Batch several data requests into one invocation

    https://iexcloud.io/docs/api/#batch-requests


    Args:
        symbols (list); List of tickers to request
        fields (list); List of fields to request
        range_ (string); Date range for chart
        last (int);
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: results in json
    '''
    x = batch(symbols, fields, range_, last, token, version, filter)

    ret = {}

    if isinstance(symbols, str):
        for field in x.keys():
            ret[field] = _MAPPING.get(field, pd.io.json.json_normalize)(x[field])
    else:
        for symbol in x.keys():
            for field in x[symbol].keys():
                if field not in ret:
                    ret[field] = pd.DataFrame()

                dat = x[symbol][field]
                dat = _MAPPING.get(field, pd.io.json.json_normalize)(dat)
                dat['symbol'] = symbol

                ret[field] = pd.concat([ret[field], dat], sort=True)
    return ret


def bulkBatch(symbols, fields=None, range_='1m', last=10, token='', version='', filter=''):
    '''Optimized batch to fetch as much as possible at once

    https://iexcloud.io/docs/api/#batch-requests


    Args:
        symbols (list); List of tickers to request
        fields (list); List of fields to request
        range_ (string); Date range for chart
        last (int);
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

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
        args.append((symbols[i:i + 99], fields, range_, last, token, version, filter))

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


def bulkBatchDF(symbols, fields=None, range_='1m', last=10, token='', version='', filter=''):
    '''Optimized batch to fetch as much as possible at once

    https://iexcloud.io/docs/api/#batch-requests


    Args:
        symbols (list); List of tickers to request
        fields (list); List of fields to request
        range_ (string); Date range for chart
        last (int);
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: results in json
    '''
    dat = bulkBatch(symbols, fields, range_, last, token, version, filter)
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


def bulkMinuteBars(symbol, dates, token='', version='', filter=''):
    '''fetch many dates worth of minute-bars for a given symbol'''
    _raiseIfNotStr(symbol)
    dates = [_strOrDate(date) for date in dates]
    list_orig = dates.__class__

    args = []
    for date in dates:
        args.append((symbol, '1d', date, token, version, filter))

    pool = ThreadPool(20)
    rets = pool.starmap(chart, args)
    pool.close()

    return list_orig(itertools.chain(*rets))


def bulkMinuteBarsDF(symbol, dates, token='', version='', filter=''):
    '''fetch many dates worth of minute-bars for a given symbol'''
    data = bulkMinuteBars(symbol, dates, token, version, filter)
    df = pd.DataFrame(data)
    if df.empty:
        return df
    _toDatetime(df)
    df.set_index(['date', 'minute'], inplace=True)
    return df

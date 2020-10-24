# -*- coding: utf-8 -*-
import pandas as pd
from functools import wraps
from ..common import _expire, _getJson, _reindex, _toDatetime, _UTC


@_expire(hour=8, tz=_UTC)
def symbols(token='', version='', filter=''):
    '''This call returns an array of symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame or list: result
    '''
    return _getJson('ref-data/symbols', token, version, filter)


@_expire(hour=8, tz=_UTC)
def iexSymbols(token='', version='', filter=''):
    '''This call returns an array of symbols the Investors Exchange supports for trading.
    This list is updated daily as of 7:45 a.m. ET. Symbols may be added or removed by the Investors Exchange after the list was produced.

    https://iexcloud.io/docs/api/#iex-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame or list: result
    '''
    return _getJson('ref-data/iex/symbols', token, version, filter)


@_expire(hour=8, tz=_UTC)
def mutualFundSymbols(token='', version='', filter=''):
    '''This call returns an array of mutual fund symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#mutual-fund-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame or list: result
    '''
    return _getJson('ref-data/mutual-funds/symbols', token, version, filter)


@_expire(hour=8, tz=_UTC)
def otcSymbols(token='', version='', filter=''):
    '''This call returns an array of OTC symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#otc-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame or list: result
    '''
    return _getJson('ref-data/otc/symbols', token, version, filter)


@_expire(hour=8, tz=_UTC)
def internationalSymbols(region='', exchange='', token='', version='', filter=''):
    '''This call returns an array of international symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#international-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        region (str): region, 2 letter case insensitive string of country codes using ISO 3166-1 alpha-2
        exchange (str): Case insensitive string of Exchange using IEX Supported Exchanges list
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame or list: result
    '''
    if region:
        return _getJson('ref-data/region/{region}/symbols'.format(region=region), token, version, filter)
    elif exchange:
        return _getJson('ref-data/exchange/{exchange}/symbols'.format(exchange=exchange), token, version, filter)
    return _getJson('ref-data/region/us/symbols', token, version, filter)


@_expire(hour=8, tz=_UTC)
def fxSymbols(token='', version=''):
    '''This call returns a list of supported currencies and currency pairs.

    https://iexcloud.io/docs/api/#fx-symbols
    7am, 9am, UTC daily

    Args:
        token (str): Access token
        version (str): API version

    Returns:
        dict or DataFrame or list: result
    '''
    return _getJson('ref-data/fx/symbols', token, version)


@_expire(hour=8, tz=_UTC)
def optionsSymbols(token='', version='', filter=''):
    '''This call returns an object keyed by symbol with the value of each symbol being an array of available contract dates.

    https://iexcloud.io/docs/api/#options-symbols
    9:30am ET Tue-Sat

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame or list: result
    '''
    return _getJson('ref-data/options/symbols', token, version, filter)


@wraps(symbols)
def symbolsDF(token='', version='', filter=''):
    df = pd.DataFrame(symbols(token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


@wraps(iexSymbols)
def iexSymbolsDF(token='', version='', filter=''):
    df = pd.DataFrame(iexSymbols(token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


@wraps(mutualFundSymbols)
def mutualFundSymbolsDF(token='', version='', filter=''):
    df = pd.DataFrame(mutualFundSymbols(token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


@wraps(otcSymbols)
def otcSymbolsDF(token='', version='', filter=''):
    df = pd.DataFrame(otcSymbols(token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


@wraps(internationalSymbols)
def internationalSymbolsDF(region='', exchange='', token='', version='', filter=''):
    df = pd.DataFrame(internationalSymbols(region, exchange, token, version, filter))
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


@wraps(fxSymbols)
def fxSymbolsDF(token='', version=''):
    fx = fxSymbols(token, version)
    df1 = pd.DataFrame(fx['currencies'])
    df2 = pd.DataFrame(fx['pairs'])
    _reindex(df1, 'code')
    return [df1, df2]


@wraps(optionsSymbols)
def optionsSymbolsDF(token='', version='', filter=''):
    df = pd.io.json.json_normalize(optionsSymbols(token, version, filter))
    df = df.T
    df.columns = ['expirations']
    return df


@wraps(symbols)
def symbolsList(token='', version=''):
    return [x['symbol'] for x in symbols(token, version, filter='symbol')]


@wraps(iexSymbols)
def iexSymbolsList(token='', version=''):
    return [x['symbol'] for x in iexSymbols(token, version, filter='symbol')]


@wraps(mutualFundSymbols)
def mutualFundSymbolsList(token='', version=''):
    return [x['symbol'] for x in mutualFundSymbols(token, version, filter='symbol')]


@wraps(otcSymbols)
def otcSymbolsList(token='', version=''):
    return [x['symbol'] for x in otcSymbols(token, version, filter='symbol')]


@wraps(internationalSymbols)
def internationalSymbolsList(region='', exchange='', token='', version=''):
    return [x['symbol'] for x in internationalSymbols(region, exchange, token, version, filter='symbol')]


@wraps(fxSymbols)
def fxSymbolsList(token='', version=''):
    fx = fxSymbols(token, version)
    ret = [[], []]
    for c in fx['currencies']:
        ret[0].append(c['code'])
    for p in fx['pairs']:
        ret[1].append(p['fromCurrency'] + p['toCurrency'])
    return ret


@wraps(optionsSymbols)
def optionsSymbolsList(token='', version=''):
    return [x['symbol'] for x in optionsSymbols(token, version, filter='symbol')]

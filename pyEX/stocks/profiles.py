# -*- coding: utf-8 -*-
import requests
import pandas as pd
from IPython.display import Image as ImageI
from io import BytesIO
from PIL import Image as ImageP
from ..common import _expire, _getJson, _raiseIfNotStr, _reindex, _toDatetime, _UTC


@_expire(hour=4, tz=_UTC)
def company(symbol, token='', version='', filter=''):
    '''Company reference data

    https://iexcloud.io/docs/api/#company
    Updates at 4am and 5am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/company', token, version, filter)


def _companyToDF(c, token='', version='', filter=''):
    '''internal'''
    df = pd.io.json.json_normalize(c)
    _toDatetime(df)
    _reindex(df, 'symbol')
    return df


def companyDF(symbol, token='', version='', filter=''):
    '''Company reference data

    https://iexcloud.io/docs/api/#company
    Updates at 4am and 5am UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    c = company(symbol, token, version, filter)
    df = _companyToDF(c)
    return df


@_expire(hour=5, tz=_UTC)
def insiderRoster(symbol, token='', version='', filter=''):
    '''Returns the top 10 insiders, with the most recent information.

    https://iexcloud.io/docs/api/#insider-roster
    Updates at 5am, 6am ET every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/insider-roster', token, version, filter)


def insiderRosterDF(symbol, token='', version='', filter=''):
    '''Returns the top 10 insiders, with the most recent information.

    https://iexcloud.io/docs/api/#insider-roster
    Updates at 5am, 6am ET every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    val = insiderRoster(symbol, token, version, filter)
    df = pd.DataFrame(val)
    _toDatetime(df, cols=[], tcols=['reportDate'])
    return df


@_expire(hour=5, tz=_UTC)
def insiderSummary(symbol, token='', version='', filter=''):
    '''Returns aggregated insiders summary data for the last 6 months.

    https://iexcloud.io/docs/api/#insider-summary
    Updates at 5am, 6am ET every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/insider-summary', token, version, filter)


def insiderSummaryDF(symbol, token='', version='', filter=''):
    '''Returns aggregated insiders summary data for the last 6 months.

    https://iexcloud.io/docs/api/#insider-summary
    Updates at 5am, 6am ET every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    val = insiderSummary(symbol, token, version, filter)
    df = pd.DataFrame(val)
    _toDatetime(df)
    return df


@_expire(hour=5, tz=_UTC)
def insiderTransactions(symbol, token='', version='', filter=''):
    '''Returns insider transactions.

    https://iexcloud.io/docs/api/#insider-transactions
    Updates at UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/insider-transactions', token, version, filter)


def insiderTransactionsDF(symbol, token='', version='', filter=''):
    '''Returns insider transactions.

    https://iexcloud.io/docs/api/#insider-transactions
    Updates at UTC every day

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    val = insiderTransactions(symbol, token, version, filter)
    df = pd.DataFrame(val)
    _toDatetime(df)
    return df


@_expire(hour=0, tz=_UTC)
def logo(symbol, token='', version='', filter=''):
    '''This is a helper function, but the google APIs url is standardized.

    https://iexcloud.io/docs/api/#logo
    8am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/logo', token, version, filter)


@_expire(hour=0, tz=_UTC)
def logoPNG(symbol, token='', version='', filter=''):
    '''This is a helper function, but the google APIs url is standardized.

    https://iexcloud.io/docs/api/#logo
    8am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        image: result as png
    '''
    _raiseIfNotStr(symbol)
    response = requests.get(logo(symbol, token, version, filter)['url'])
    return ImageP.open(BytesIO(response.content))


@_expire(hour=0, tz=_UTC)
def logoNotebook(symbol, token='', version='', filter=''):
    '''This is a helper function, but the google APIs url is standardized.

    https://iexcloud.io/docs/api/#logo
    8am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        image: result
    '''
    _raiseIfNotStr(symbol)
    url = logo(symbol, token, version, filter)['url']
    return ImageI(url=url)


@_expire(hour=8, tz=_UTC)
def peers(symbol, token='', version='', filter=''):
    '''Peers of ticker

    https://iexcloud.io/docs/api/#peers
    8am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/peers', token, version, filter)


def _peersToDF(p):
    '''internal'''
    df = pd.DataFrame(p, columns=['symbol'])
    _toDatetime(df)
    _reindex(df, 'symbol')
    df['peer'] = df.index
    return df


def peersDF(symbol, token='', version='', filter=''):
    '''Peers of ticker

    https://iexcloud.io/docs/api/#peers
    8am UTC daily

    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    p = peers(symbol, token, version, filter)
    df = _peersToDF(p)
    return df


@_expire(hour=8, tz=_UTC)
def relevant(symbol, token='', version='', filter=''):
    '''Same as peers

    https://iexcloud.io/docs/api/#relevant
    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    _raiseIfNotStr(symbol)
    return _getJson('stock/' + symbol + '/relevant', token, version, filter)


def relevantDF(symbol, token='', version='', filter=''):
    '''Same as peers

    https://iexcloud.io/docs/api/#relevant
    Args:
        symbol (string); Ticker to request
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    df = pd.DataFrame(relevant(symbol, token, version, filter))
    _toDatetime(df)
    return df

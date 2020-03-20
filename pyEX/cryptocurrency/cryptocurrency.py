# -*- coding: utf-8 -*-
import pandas as pd
from ..common import _getJson


def cryptoBook(symbol, token='', version='', filter=''):
    '''This returns a current snapshot of the book for a specified cryptocurrency. For REST, you will receive a current snapshot of the current book for the specific cryptocurrency. For SSE Streaming, you will get a full representation of the book updated as often as the book changes. Examples of each are below:

    https://iexcloud.io/docs/api/#cryptocurrency-book
    continuous

    Args:
        symbol (string); cryptocurrency ticker
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('/crypto/{symbol}/book'.format(symbol=symbol), token, version, filter)


def cryptoBookDF(symbol, token='', version='', filter=''):
    '''This returns a current snapshot of the book for a specified cryptocurrency. For REST, you will receive a current snapshot of the current book for the specific cryptocurrency. For SSE Streaming, you will get a full representation of the book updated as often as the book changes. Examples of each are below:

    https://iexcloud.io/docs/api/#cryptocurrency-book
    continuous

    Args:
        symbol (string); cryptocurrency ticker
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(cryptoBook(symbol, token, version, filter))


def cryptoPrice(symbol, token='', version='', filter=''):
    '''This returns the price for a specified cryptocurrency.

    https://iexcloud.io/docs/api/#cryptocurrency-price
    continuous

    Args:
        symbol (string); cryptocurrency ticker
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('/crypto/{symbol}/price'.format(symbol=symbol), token, version, filter)


def cryptoPriceDF(symbol, token='', version='', filter=''):
    '''This returns the price for a specified cryptocurrency.

    https://iexcloud.io/docs/api/#cryptocurrency-price
    continuous

    Args:
        symbol (string); cryptocurrency ticker
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(cryptoPrice(symbol, token, version, filter))


def cryptoQuote(symbol, token='', version='', filter=''):
    '''This returns the quote for a specified cryptocurrency. Quotes are available via REST and SSE Streaming.


    https://iexcloud.io/docs/api/#cryptocurrency-quote
    continuous

    Args:
        symbol (string); cryptocurrency ticker
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict: result
    '''
    return _getJson('/crypto/{symbol}/price'.format(symbol=symbol), token, version, filter)


def cryptoQuoteDF(symbol, token='', version='', filter=''):
    '''This returns the quote for a specified cryptocurrency. Quotes are available via REST and SSE Streaming.

    https://iexcloud.io/docs/api/#cryptocurrency-quote
    continuous

    Args:
        symbol (string); cryptocurrency ticker
        token (string); Access token
        version (string); API version
        filter (string); filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        DataFrame: result
    '''
    return pd.DataFrame(cryptoQuote(symbol, token, version, filter))

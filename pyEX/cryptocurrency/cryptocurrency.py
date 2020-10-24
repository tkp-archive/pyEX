# -*- coding: utf-8 -*-
import pandas as pd
from functools import wraps
from ..common import _getJson


def cryptoBook(symbol, token='', version='', filter=''):
    '''This returns a current snapshot of the book for a specified cryptocurrency. For REST, you will receive a current snapshot of the current book for the specific cryptocurrency. For SSE Streaming, you will get a full representation of the book updated as often as the book changes. Examples of each are below:

    https://iexcloud.io/docs/api/#cryptocurrency-book
    continuous

    Args:
        symbol (str): cryptocurrency ticker
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return _getJson('/crypto/{symbol}/book'.format(symbol=symbol), token, version, filter)


@wraps(cryptoBook)
def cryptoBookDF(symbol, token='', version='', filter=''):
    return pd.DataFrame(cryptoBook(symbol, token, version, filter))


def cryptoPrice(symbol, token='', version='', filter=''):
    '''This returns the price for a specified cryptocurrency.

    https://iexcloud.io/docs/api/#cryptocurrency-price
    continuous

    Args:
        symbol (str): cryptocurrency ticker
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return _getJson('/crypto/{symbol}/price'.format(symbol=symbol), token, version, filter)


@wraps(cryptoPrice)
def cryptoPriceDF(symbol, token='', version='', filter=''):
    return pd.DataFrame(cryptoPrice(symbol, token, version, filter))


def cryptoQuote(symbol, token='', version='', filter=''):
    '''This returns the quote for a specified cryptocurrency. Quotes are available via REST and SSE Streaming.


    https://iexcloud.io/docs/api/#cryptocurrency-quote
    continuous

    Args:
        symbol (str): cryptocurrency ticker
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results

    Returns:
        dict or DataFrame: result
    '''
    return _getJson('/crypto/{symbol}/price'.format(symbol=symbol), token, version, filter)


@wraps(cryptoQuote)
def cryptoQuoteDF(symbol, token='', version='', filter=''):
    return pd.DataFrame(cryptoQuote(symbol, token, version, filter))

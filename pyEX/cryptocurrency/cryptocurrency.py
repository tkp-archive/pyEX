# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _get, _getAsync


def cryptoBook(symbol, token="", version="stable", filter="", format="json"):
    """This returns a current snapshot of the book for a specified cryptocurrency. For REST, you will receive a current snapshot of the current book for the specific cryptocurrency. For SSE Streaming, you will get a full representation of the book updated as often as the book changes. Examples of each are below:

    https://iexcloud.io/docs/api/#cryptocurrency-book
    continuous

    Args:
        symbol (str): cryptocurrency ticker
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get(
        "/crypto/{symbol}/book".format(symbol=symbol),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(cryptoBook)
def cryptoBookDF(*args, **kwargs):
    return pd.DataFrame(cryptoBook(*args, **kwargs))


@wraps(cryptoBook)
async def cryptoBookAsync(symbol, token="", version="stable", filter="", format="json"):
    return _getAsync(
        "/crypto/{symbol}/book".format(symbol=symbol),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def cryptoPrice(symbol, token="", version="stable", filter="", format="json"):
    """This returns the price for a specified cryptocurrency.

    https://iexcloud.io/docs/api/#cryptocurrency-price
    continuous

    Args:
        symbol (str): cryptocurrency ticker
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get(
        "/crypto/{symbol}/price".format(symbol=symbol),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(cryptoPrice)
def cryptoPriceDF(*args, **kwargs):
    return pd.DataFrame(cryptoPrice(*args, **kwargs))


@wraps(cryptoPrice)
async def cryptoPriceAsync(
    symbol, token="", version="stable", filter="", format="json"
):
    return await _getAsync(
        "/crypto/{symbol}/price".format(symbol=symbol),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def cryptoQuote(symbol, token="", version="stable", filter="", format="json"):
    """This returns the quote for a specified cryptocurrency. Quotes are available via REST and SSE Streaming.


    https://iexcloud.io/docs/api/#cryptocurrency-quote
    continuous

    Args:
        symbol (str): cryptocurrency ticker
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get(
        "/crypto/{symbol}/quote".format(symbol=symbol),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(cryptoQuote)
def cryptoQuoteDF(*args, **kwargs):
    return pd.DataFrame(cryptoQuote(*args, **kwargs))


@wraps(cryptoQuote)
async def cryptoQuoteAsync(
    symbol, token="", version="stable", filter="", format="json"
):
    return await _getAsync(
        "/crypto/{symbol}/quote".format(symbol=symbol),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )

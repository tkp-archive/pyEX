# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _get, _post, _raiseIfNotStr, _quoteSymbols, _delete


def getWatchlist(
    id="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """
    Args:
        id (str): watchlist ID
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
        dict: result
    """
    url = "/account/watchlist"

    if id:
        url += "/{}/contents".format(id)
    return _get(url=url, token=token, version=version, filter=filter, format=format)


@wraps(getWatchlist)
def getWatchlistDF(*args, **kwargs):
    return pd.DataFrame(getWatchlist(*args, **kwargs))


def createWatchlist(
    token="",
    version="stable",
    filter="",
    format="json",
):
    """
    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
        dict: result
    """
    url = "/account/watchlist"
    return _post(url=url, token=token, version=version, filter=filter, format=format)


def addToWatchlist(
    id,
    symbol,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """
    Args:
        id (str): watchlist ID
        symbol (str): Symbol to add to watchlist
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
        dict: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    url = "/account/watchlist/{}/contents?symbol={}".format(id, symbol)
    return _post(url=url, token=token, version=version, filter=filter, format=format)


def deleteFromWatchlist(
    id,
    symbol,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """
    Args:
        id (str): watchlist ID
        symbol (str): Symbol to add to watchlist
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
        dict: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    url = "/account/watchlist/{}/contents?symbol={}".format(id, symbol)
    return _delete(url=url, token=token, version=version, filter=filter, format=format)


def deleteWatchlist(
    id,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """
    Args:
        id (str): watchlist ID
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
        dict: result
    """
    url = "/account/watchlist/{}".format(id)
    return _delete(url=url, token=token, version=version, filter=filter, format=format)

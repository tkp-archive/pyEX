# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
import pandas as pd

from functools import wraps

from ...common import _UTC, _expire, _get, json_normalize


@_expire(hour=8, tz=_UTC)
def optionsSymbols(
    symbol="",
    expiration="",
    includeExpired=None,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This call returns an object keyed by symbol with the value of each symbol being an array of available contract dates.

    https://iexcloud.io/docs/api/#options-symbols
    9:30am ET Tue-Sat

    Args:
        symbol (str): underlying symbol
        expiration (str): expiration date
        includeExpired (bool): Include expired contracts in result
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    if symbol:
        url = "ref-data/options/symbols/{}".format(symbol)

        if expiration:
            url += "/{}".format(expiration)

        if includeExpired is not None:
            url += "?includeExpired={}".format(includeExpired)
    else:
        url = "ref-data/options/symbols"

    return _get(
        url,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(optionsSymbols)
def optionsSymbolsDF(symbol="", *args, **kwargs):
    if symbol:
        df = pd.DataFrame(optionsSymbols(symbol, *args, **kwargs))
    else:
        df = json_normalize(optionsSymbols(*args, **kwargs)).T
    return df


@wraps(optionsSymbols)
def optionsSymbolsList(symbol="", *args, **kwargs):
    kwargs["filter"] = "symbol"
    symbols = optionsSymbols(symbol, *args, **kwargs)
    if symbol:
        ret = [symbol["symbol"] for symbol in symbols]
    else:
        ret = []
        for ticker, dates in symbols.items():
            for date in dates:
                ret.append("{}-{}".format(ticker, date))
    return ret

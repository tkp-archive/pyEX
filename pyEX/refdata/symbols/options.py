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


# @_expire(hour=8, tz=_UTC)
# def optionsSymbols(token="", version="stable", filter="", format="json"):
#     """This call returns an object keyed by symbol with the value of each symbol being an array of available contract dates.

#     https://iexcloud.io/docs/api/#options-symbols
#     9:30am ET Tue-Sat

#     Args:
#         token (str): Access token
#         version (str): API version
#         filter (str): filters: https://iexcloud.io/docs/api/#filter-results
#         format (str): return format, defaults to json

#     Returns:
#         dict or DataFrame or list: result
#     """
#     return _get(
#         "ref-data/options/symbols",
#         token=token,
#         version=version,
#         filter=filter,
#         format=format,
#     )


# @wraps(optionsSymbols)
# def optionsSymbolsDF(*args, **kwargs):
#     df = json_normalize(optionsSymbols(*args, **kwargs))
#     df = df.T
#     df.columns = ["expirations"]
#     df.sort_index(inplace=True)
#     return df


# @wraps(optionsSymbols)
# def optionsSymbolsList(*args, **kwargs):
#     kwargs["filter"] = "symbol"
#     symbols = optionsSymbols(*args, **kwargs)
#     ret = []
#     for ticker, dates in symbols.items():
#         for date in dates:
#             ret.append("{}-{}".format(ticker, date))
#     return ret


def optionsSymbols(
    symbol="", token="", version="stable", filter="", format="json"
):
    """This call returns an object keyed by symbol with the value of each symbol being an array of available contract dates.

    https://iexcloud.io/docs/api/#options-symbols
    9:30am ET Tue-Sat

    Args:
        symbol (str): underlying symbol
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    if symbol:
        return _get(
            "ref-data/options/symbols/{}".format(symbol),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "ref-data/options/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(optionsSymbols)
def optionsSymbolsDF(*args, **kwargs):
    if "new" in kwargs:
        df = pd.DataFrame(optionsSymbols(*args, **kwargs))
    else:
        df = json_normalize(optionsSymbols(*args, **kwargs))
    return df


@wraps(optionsSymbols)
def optionsSymbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    symbols = optionsSymbols(*args, **kwargs)
    ret = []
    for ticker, dates in symbols.items():
        for date in dates:
            ret.append("{}-{}".format(ticker, date))
    return ret

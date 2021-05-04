# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ...common import _UTC, _expire, _get, _reindex


@_expire(hour=8, tz=_UTC)
def fxSymbols(token="", version="stable", filter="", format="json"):
    """This call returns a list of supported currencies and currency pairs.

    https://iexcloud.io/docs/api/#fx-symbols
    7am, 9am, UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/fx/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(fxSymbols)
def fxSymbolsDF(token="", version="stable"):
    fx = fxSymbols(token, version)
    df1 = pd.DataFrame(fx["currencies"])
    df2 = pd.DataFrame(fx["pairs"])
    _reindex(df1, "code")
    df1.sort_index(inplace=True)
    df2.sort_index(inplace=True)
    return [df1, df2]


@wraps(fxSymbols)
def fxSymbolsList(*args, **kwargs):
    fx = fxSymbols(*args, **kwargs)
    ret = [[], []]
    for c in fx["currencies"]:
        ret[0].append(c["code"])
    for p in fx["pairs"]:
        ret[1].append(p["fromCurrency"] + p["toCurrency"])
    return sorted(ret)

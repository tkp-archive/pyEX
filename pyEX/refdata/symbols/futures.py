# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ...common import _UTC, _expire, _get, _reindex, _toDatetime


@_expire(hour=8, tz=_UTC)
def futuresSymbols(
    underlying="",
    includeExpired=None,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This call returns an array of futures symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#futures-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        underlying (str): Underlying asset
        includeExpired (bool): Include expired contracts in result
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    url = "ref-data/futures/symbols{}".format(
        "/{}".format(underlying) if underlying else ""
    )
    if includeExpired is not None:
        url += "?includeExpired={}".format(includeExpired)

    return _get(
        url,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(futuresSymbols)
def futuresSymbolsDF(*args, **kwargs):
    df = pd.DataFrame(futuresSymbols(*args, **kwargs))
    _toDatetime(df)
    _reindex(df, "symbol")
    df.sort_index(inplace=True)
    return df


@wraps(futuresSymbols)
def futuresSymbolsList(*args, **kwargs):
    if args or kwargs.get("underlying"):
        grab = "symbol"
    else:
        grab = "underlying"
    kwargs["filter"] = grab
    return sorted([x[grab] for x in futuresSymbols(*args, **kwargs)])

# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _UTC, _expire, _get, _reindex, _toDatetime


@_expire(hour=8, tz=_UTC)
def otcSymbols(token="", version="stable", filter="", format="json"):
    """This call returns an array of OTC symbols that IEX Cloud supports for API calls.

    https://iexcloud.io/docs/api/#otc-symbols
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/otc/symbols",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(otcSymbols)
def otcSymbolsDF(*args, **kwargs):
    df = _reindex(_toDatetime(pd.DataFrame(otcSymbols(*args, **kwargs))), "symbol")
    df.sort_index(inplace=True)
    return df


@wraps(otcSymbols)
def otcSymbolsList(*args, **kwargs):
    kwargs["filter"] = "symbol"
    return sorted([x["symbol"] for x in otcSymbols(*args, **kwargs)])

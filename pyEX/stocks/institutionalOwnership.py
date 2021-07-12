# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import (
    _EST,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _toDatetime,
)


@_expire(hour=5, tz=_EST)
def institutionalOwnership(
    symbol, token="", version="stable", filter="", format="json"
):
    """Returns the top 10 institutional holders, defined as buy-side or sell-side firms.

    https://iexcloud.io/docs/api/#institutional-ownership
    Updates at 5am, 6am ET every day

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    return _get(
        "stock/{symbol}/institutional-ownership".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(institutionalOwnership)
def institutionalOwnershipDF(*args, **kwargs):
    return _toDatetime(
        pd.DataFrame(institutionalOwnership(*args, **kwargs)),
        cols=[],
        tcols=["reportDate"],
    )

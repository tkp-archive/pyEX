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
    _UTC,
    _checkPeriodLast,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _toDatetime,
)


@_expire(hour=8, tz=_UTC)
def fundamentals(
    symbol, period="quarter", token="", version="stable", filter="", format="json"
):
    """Pulls fundamentals data.

    https://iexcloud.io/docs/api/#advanced-fundamentals
    Updates at 8am, 9am UTC daily

    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _checkPeriodLast(period, 1)
    return _get(
        "stock/{}/fundamentals?period={}".format(symbol, period),
        token=token,
        version=version,
        filter=filter,
        format=format,
    ).get("fundamentals", [])


def _fundamentalsToDF(f):
    """internal"""
    if f:
        df = _reindex(_toDatetime(pd.DataFrame(f)), "reportDate")
    else:
        df = pd.DataFrame()
    return df


@wraps(fundamentals)
def fundamentalsDF(*args, **kwargs):
    return _fundamentalsToDF(fundamentals(*args, **kwargs))

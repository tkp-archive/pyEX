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
def financials(
    symbol, period="quarter", token="", version="stable", filter="", format="json"
):
    """Pulls income statement, balance sheet, and cash flow data from the four most recent reported quarters.

    https://iexcloud.io/docs/api/#financials
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
        "stock/{}/financials?period={}".format(symbol, period),
        token=token,
        version=version,
        filter=filter,
        format=format,
    ).get("financials", [])


def _financialsToDF(f):
    """internal"""
    if f:
        df = _reindex(_toDatetime(pd.DataFrame(f)), "reportDate")
    else:
        df = pd.DataFrame()
    return df


@wraps(financials)
def financialsDF(*args, **kwargs):
    return _financialsToDF(financials(*args, **kwargs))

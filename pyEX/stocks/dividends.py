# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _quoteSymbols, _raiseIfNotStr, _timeseriesWrapper, _expire, _UTC
from ..timeseries import timeSeries


@_expire(hour=8, tz=_UTC)
def dividends(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Obtain up-to-date and detailed information on all new dividend announcements, as well as 12+ years of historical dividend records. This endpoint covers over 39,000 US equities, mutual funds, ADRs, and ETFs.
    You’ll be provided with:
        Detailed information on both cash and stock dividends including record, payment, ex, and announce dates
        Gross and net amounts
        Details of all currencies in which a dividend can be paid
        Tax information
        The ability to keep up with the growing number of complex dividend distributions

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#dividends

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_dividends",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(dividends)
def dividendsDF(*args, **kwargs):
    return pd.DataFrame(dividends(*args, **kwargs))

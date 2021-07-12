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
def returnOfCapital(
    symbol="",
    refid="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Return of capital up-to-date and detailed information on all new announcements, as well as 12+ years of historical records.

    Updated at 5am, 10am, 8pm UTC daily

    https://iexcloud.io/docs/api/#return-of-capital

    Args:
        symbol (str): Symbol to look up
        refid (str): Optional. Id that matches the refid field returned in the response object. This allows you to pull a specific event for a symbol.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="advanced_return_of_capital",
        key=symbol,
        subkey=refid,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(returnOfCapital)
def returnOfCapitalDF(*args, **kwargs):
    return pd.DataFrame(returnOfCapital(*args, **kwargs))

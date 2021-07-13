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
def fundamentalValuations(
    symbol="",
    frequency="",
    token="",
    version="stable",
    filter="",
    format="json",
    **timeseries_kwargs
):
    """Fundamental Valuations

    Args:
        symbol (str): Symbol to look up
        frequency (str): Optional.
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
        id="fundamental_valuations",
        key=symbol,
        subkey=frequency,
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(fundamentalValuations)
def fundamentalValuationsDF(*args, **kwargs):
    return pd.DataFrame(fundamentalValuations(*args, **kwargs))

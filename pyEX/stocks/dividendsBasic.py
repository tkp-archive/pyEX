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
    _TIMEFRAME_DIVSPLIT,
    _UTC,
    PyEXception,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _toDatetime,
)


@_expire(hour=9, tz=_UTC)
def dividendsBasic(
    symbol,
    timeframe="ytd",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Dividend history

    https://iexcloud.io/docs/api/#dividends
    Updated at 9am UTC every day

    Args:
        symbol (str): Ticker to request
        timeframe (str): timeframe for data
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    if timeframe not in _TIMEFRAME_DIVSPLIT:
        raise PyEXception("Range must be in %s" % str(_TIMEFRAME_DIVSPLIT))
    return _get(
        "stock/" + symbol + "/dividends/" + timeframe,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def _dividendsToDF(d):
    return _reindex(_toDatetime(pd.DataFrame(d)), "exDate")


@wraps(dividendsBasic)
def dividendsBasicDF(*args, **kwargs):
    return _dividendsToDF(dividendsBasic(*args, **kwargs))

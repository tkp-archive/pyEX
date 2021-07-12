# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import numpy as np
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
def cashFlow(
    symbol,
    period="quarter",
    last=1,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Pulls cash flow data. Available quarterly (4 quarters) or annually (4 years).

    https://iexcloud.io/docs/api/#cash-flow
    Updates at 8am, 9am UTC daily


    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)
    _checkPeriodLast(period, last)
    return _get(
        "stock/{}/cash-flow?period={}&last={}".format(symbol, period, last),
        token=token,
        version=version,
        filter=filter,
        format=format,
    ).get("cashflow", [])


@wraps(cashFlow)
def cashFlowDF(*args, **kwargs):
    df = _reindex(
        _toDatetime(pd.DataFrame(cashFlow(*args, **kwargs))),
        "reportDate",
    )
    df.replace(to_replace=[None], value=np.nan, inplace=True)
    return df

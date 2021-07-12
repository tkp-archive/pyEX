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
    _checkPeriodLast,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _toDatetime,
    json_normalize,
)


def estimates(
    symbol,
    period="quarter",
    last=1,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Provides the latest consensus estimate for the next fiscal period

    https://iexcloud.io/docs/api/#estimates
    Updates at 9am, 11am, 12pm UTC every day

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
    _checkPeriodLast(period, last)
    return _get(
        "stock/{}/estimates?period={}&last={}".format(
            _quoteSymbols(symbol), period, last
        ),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def _estimatesToDF(f):
    """internal"""
    if f:
        df = _reindex(
            _toDatetime(json_normalize(f, "estimates", "symbol")), "fiscalEndDate"
        )
    else:
        df = pd.DataFrame()
    return df


@wraps(estimates)
def estimatesDF(*args, **kwargs):
    return _estimatesToDF(estimates(*args, **kwargs))

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
    json_normalize,
)


@_expire(hour=9, tz=_UTC)
def earnings(
    symbol,
    period="quarter",
    last=1,
    field="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Earnings data for a given company including the actual EPS, consensus, and fiscal period. Earnings are available quarterly (last 4 quarters) and annually (last 4 years).

    https://iexcloud.io/docs/api/#earnings
    Updates at 9am, 11am, 12pm UTC every day

    Args:
        symbol (str): Ticker to request
        period (str): Period, either 'annual' or 'quarter'
        last (int): Number of records to fetch, up to 12 for 'quarter' and 4 for 'annual'
        field (str): Subfield to fetch
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
    if not field:
        return _get(
            "stock/{}/earnings?period={}&last={}".format(symbol, period, last),
            token=token,
            version=version,
            filter=filter,
            format=format,
        ).get("earnings", [])
    return _get(
        "stock/{}/earnings/{}/{}?period={}".format(symbol, last, field, period),
        token=token,
        version=version,
        filter=filter,
        format=format,
    ).get("earnings", [])


def _earningsToDF(e):
    """internal"""
    if e:
        df = _reindex(_toDatetime(pd.DataFrame(e)), "EPSReportDate")
    else:
        df = pd.DataFrame()
    return df


@wraps(earnings)
def earningsDF(*args, **kwargs):
    return _earningsToDF(earnings(*args, **kwargs))


@_expire(minute=0)
def earningsToday(token="", version="stable", filter="", format="json"):
    """Returns earnings that will be reported today as two arrays: before the open bto and after market close amc.
    Each array contains an object with all keys from earnings, a quote object, and a headline key.

    https://iexcloud.io/docs/api/#earnings-today
    Updates at 9am, 11am, 12pm UTC daily


    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/today-earnings", token, version, filter)


@wraps(earningsToday)
def earningsTodayDF(*args, **kwargs):
    x = earningsToday(*args, **kwargs)
    z = []
    for k in x:
        ds = x[k]
        for d in ds:
            d["when"] = k
            z.extend(ds)
    df = json_normalize(z)

    if not df.empty:
        df.drop_duplicates(inplace=True)
    return _reindex(_toDatetime(df), "symbol")

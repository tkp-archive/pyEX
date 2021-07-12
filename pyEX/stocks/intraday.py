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
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _strOrDate,
    _toDatetime,
)


def intraday(
    symbol,
    date="",
    exactDate="",
    last=-1,
    IEXOnly=False,
    reset=False,
    simplify=False,
    interval=-1,
    changeFromClose=False,
    IEXWhenNull=False,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This endpoint will return aggregated intraday prices in one minute buckets

    https://iexcloud.io/docs/api/#intraday-prices
    9:30-4pm ET Mon-Fri on regular market trading days
    9:30-1pm ET on early close trading days

    Args:
        symbol (str): Ticker to request
        date (str): Formatted as YYYYMMDD. This can be used for batch calls when range is 1d or date. Currently supporting trailing 30 calendar days of minute bar data.
        exactDate (str): Same as `date`, takes precedence
        last (number): If passed, chart data will return the last N elements
        IEXOnly (bool): Limits the return of intraday prices to IEX only data.
        reset (bool): If true, chart will reset at midnight instead of the default behavior of 9:30am ET.
        simplify (bool): If true, runs a polyline simplification using the Douglas-Peucker algorithm. This is useful if plotting sparkline charts.
        interval (number): If passed, chart data will return every Nth element as defined by chartInterval
        changeFromClose (bool): If true, changeOverTime and marketChangeOverTime will be relative to previous day close instead of the first value.
        IEXWhenNull (bool): By default, all market prefixed fields are 15 minute delayed, meaning the most recent 15 objects will be null. If this parameter is passed as true, all market prefixed fields that are null will be populated with IEX data if available.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    symbol = _quoteSymbols(symbol)

    # exactDate takes precedence
    date = exactDate or date
    if date:
        date = _strOrDate(date)

    # Assemble params
    params = {}

    if date:
        params["exactDate"] = date

    if last > 0:
        params["chartLast"] = last

    if IEXOnly:
        params["chartIEXOnly"] = IEXOnly

    if reset:
        params["chartReset"] = reset

    if simplify:
        params["chartSimplify"] = simplify

    if interval > 0:
        params["chartInterval"] = interval

    if changeFromClose:
        params["changeFromClose"] = changeFromClose

    if IEXWhenNull:
        params["chartIEXWhenNull"] = IEXWhenNull

    base_url = "stock/{}/intraday-prices?".format(symbol)

    if params:
        base_url += "&".join("{}={}".format(k, v) for k, v in params.items())
    return _get(base_url, token=token, version=version, filter=filter, format=format)


@wraps(intraday)
def intradayDF(*args, **kwargs):
    val = intraday(*args, **kwargs)
    df = _toDatetime(pd.DataFrame(val))
    if not df.empty and "date" in df.columns and "minute" in df.columns:
        df.set_index(["date", "minute"], inplace=True)
    elif not df.empty and "date" in df.columns:
        _reindex(df, "date")
    else:
        df = pd.DataFrame()
    return df

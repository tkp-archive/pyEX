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
    _EST,
    _RANGE_CHART,
    PyEXception,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _strOrDate,
    _toDatetime,
)


@_expire(hour=4, tz=_EST)
def chart(
    symbol,
    range="1m",
    date=None,
    exactDate=None,
    last=-1,
    closeOnly=False,
    byDay=False,
    simplify=False,
    interval=-1,
    changeFromClose=False,
    displayPercent=False,
    sort="desc",
    includeToday=False,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Historical price/volume data, daily and intraday

    https://iexcloud.io/docs/api/#historical-prices
    Data Schedule
    1d: -9:30-4pm ET Mon-Fri on regular market trading days
        -9:30-1pm ET on early close trading days
    All others:
        -Prior trading day available after 4am ET Tue-Sat

    Args:
        symbol (str): Ticker to request
        range (str): Range to request e.g. 1m
        date (datetime): date, if requesting intraday
        exactDate (str): Same as `date`, takes precedence
        last (int): If passed, chart data will return the last N elements from the time period defined by the range parameter
        closeOnly (bool): Will return adjusted data only with keys date, close, and volume.
        byDay (bool): Used only when range is date to return OHLCV data instead of minute bar data.
        simplify (bool) If true, runs a polyline simplification using the Douglas-Peucker algorithm. This is useful if plotting sparkline charts.
        interval (int) If passed, chart data will return every Nth element as defined by chartInterval
        changeFromClose (bool): If true, changeOverTime and marketChangeOverTime will be relative to previous day close instead of the first value.
        displayPercent (bool): If set to true, all percentage values will be multiplied by a factor of 100 (Ex: /stock/twtr/chart?displayPercent=true)
        range (str): Same format as the path parameter. This can be used for batch calls.
        sort (str): Can be "asc" or "desc" to sort results by date. Defaults to "desc"
        includeToday (bool): If true, current trading day data is appended
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)

    base_url = "stock/{}/chart/{}?".format(_quoteSymbols(symbol), range)

    # exactDate takes precedence
    date = exactDate or date
    if date:
        date = _strOrDate(date)

    if range is not None and range != "1d":
        if range not in _RANGE_CHART:
            raise PyEXception("Range must be in {}".format(_RANGE_CHART))

    # Assemble params
    params = {}

    # TODO need these?
    # if date:
    #     params["exactDate"] = date
    # if range:
    #     params["range"] = range

    if last > 0:
        params["chartLast"] = last

    if closeOnly:
        params["chartCloseOnly"] = closeOnly

    if byDay:
        params["chartByDay"] = byDay

    if simplify:
        params["chartSimplify"] = simplify

    if interval > 0:
        params["chartInterval"] = interval

    if changeFromClose:
        params["changeFromClose"] = changeFromClose

    if displayPercent:
        params["displayPercent"] = displayPercent

    if exactDate:
        params["exactDate"] = exactDate

    if sort:
        if sort.lower() not in (
            "asc",
            "desc",
        ):
            raise PyEXception("Sort must be in (asc, desc), got: {}".format(sort))

        params["sort"] = sort.lower()

    if includeToday:
        params["includeToday"] = includeToday

    if date:
        base_url = "stock/{}/chart/date/{}?".format(_quoteSymbols(symbol), date)

        if params:
            base_url += "&".join("{}={}".format(k, v) for k, v in params.items())
        return _get(
            base_url, token=token, version=version, filter=filter, format=format
        )

    if params:
        base_url += "&".join("{}={}".format(k, v) for k, v in params.items())

    return _get(base_url, token=token, version=version, filter=filter, format=format)


def _chartToDF(c):
    """internal"""
    return _reindex(_toDatetime(pd.DataFrame(c)), "date")


@wraps(chart)
def chartDF(
    symbol,
    range="1m",
    date=None,
    exactDate=None,
    last=-1,
    closeOnly=False,
    byDay=False,
    simplify=False,
    interval=-1,
    changeFromClose=False,
    displayPercent=False,
    sort="desc",
    includeToday=False,
    token="",
    version="stable",
    filter="",
    format="json",
):
    c = chart(
        symbol=symbol,
        range=range,
        date=date,
        exactDate=exactDate,
        last=last,
        closeOnly=closeOnly,
        byDay=byDay,
        simplify=simplify,
        interval=interval,
        changeFromClose=changeFromClose,
        displayPercent=displayPercent,
        sort=sort,
        includeToday=includeToday,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )
    df = _toDatetime(pd.DataFrame(c))
    if range is not None and range != "1d":
        _reindex(df, "date")
    else:
        if not df.empty and "date" in df.columns and "minute" in df.columns:
            df.set_index(["date", "minute"], inplace=True)
        elif not df.empty and "date" in df.columns:
            _reindex(df, "date")
        elif not df.empty:
            # Nothing to do
            ...
        else:
            df = pd.DataFrame()
    return df

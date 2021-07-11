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
    _KEY_STATS,
    PyEXception,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _toDatetime,
    json_normalize,
)


@_expire(hour=8, tz=_EST)
def keyStats(symbol, stat="", token="", version="stable", filter="", format="json"):
    """Key Stats about company

    https://iexcloud.io/docs/api/#key-stats
    8am, 9am ET

    Args:
        symbol (str): Ticker to request
        stat   (Optiona[str]): specific stat to request, in:
                                companyName
                                marketcap
                                week52high
                                week52low
                                week52change
                                sharesOutstanding
                                float
                                avg10Volume
                                avg30Volume
                                day200MovingAvg
                                day50MovingAvg
                                employees
                                ttmEPS
                                ttmDividendRate
                                dividendYield
                                nextDividendDate
                                exDividendDate
                                nextEarningsDate
                                peRatio
                                beta
                                maxChangePercent
                                year5ChangePercent
                                year2ChangePercent
                                year1ChangePercent
                                ytdChangePercent
                                month6ChangePercent
                                month3ChangePercent
                                month1ChangePercent
                                day30ChangePercent
                                day5ChangePercent
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    if stat:
        if stat not in _KEY_STATS:
            raise PyEXception("Stat must be in {}".format(_KEY_STATS))
        return _get(
            "stock/{}/stats/{}".format(_quoteSymbols(symbol), stat),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "stock/{}/stats".format(_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def _statsToDF(s):
    """internal"""
    if s:
        df = _reindex(_toDatetime(json_normalize(s)), "symbol")
    else:
        df = pd.DataFrame()
    return df


@wraps(keyStats)
def keyStatsDF(*args, **kwargs):
    return _statsToDF(keyStats(*args, **kwargs))

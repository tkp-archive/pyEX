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
    _expire,
    _get,
    _reindex,
    _toDatetime,
    json_normalize,
)


@_expire(hour=10, tz=_UTC)
def ipoToday(token="", version="stable", filter="", format="json"):
    """This returns a list of upcoming or today IPOs scheduled for the current and next month. The response is split into two structures:
    rawData and viewData. rawData represents all available data for an IPO. viewData represents data structured for display to a user.

    https://iexcloud.io/docs/api/#ipo-calendar
    10am, 10:30am UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/today-ipos", token, version, filter)


@wraps(ipoToday)
def ipoTodayDF(*args, **kwargs):
    val = ipoToday(*args, **kwargs)
    if val:
        df = _reindex(_toDatetime(json_normalize(val, "rawData")), "symbol")
    else:
        df = pd.DataFrame()
    return df


@_expire(hour=10)
def ipoUpcoming(token="", version="stable", filter="", format="json"):
    """This returns a list of upcoming or today IPOs scheduled for the current and next month. The response is split into two structures:
    rawData and viewData. rawData represents all available data for an IPO. viewData represents data structured for display to a user.

    https://iexcloud.io/docs/api/#ipo-calendar
    10am, 10:30am UTC daily

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get("stock/market/upcoming-ipos", token, version, filter)


@wraps(ipoUpcoming)
def ipoUpcomingDF(*args, **kwargs):
    val = ipoUpcoming(*args, **kwargs)
    if val:
        df = _reindex(_toDatetime(json_normalize(val, "rawData")), "symbol")
    else:
        df = pd.DataFrame()
    return df

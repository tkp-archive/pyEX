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
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _strOrDate,
    _toDatetime,
)


@_expire(hour=16, tz=_EST)
def marketShortInterest(
    date=None, token="", version="stable", filter="", format="json"
):
    """The consolidated market short interest positions in all IEX-listed securities are included in the IEX Short Interest Report.

    The report data will be published daily at 4:00pm ET.

    https://iexcloud.io/docs/api/#listed-short-interest-list-in-dev

    Args:
        date (datetime): Effective Datetime
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    if date:
        date = _strOrDate(date)
        return _get("stock/market/short-interest/" + date, token, version, filter)
    return _get("stock/market/short-interest", token, version, filter)


@wraps(marketShortInterest)
def marketShortInterestDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(marketShortInterest(*args, **kwargs)))


@_expire(hour=16, tz=_EST)
def shortInterest(
    symbol,
    date=None,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """The consolidated market short interest positions in all IEX-listed securities are included in the IEX Short Interest Report.

    The report data will be published daily at 4:00pm ET.

    https://iexcloud.io/docs/api/#listed-short-interest-list-in-dev

    Args:
        symbol (str): Ticker to request
        date (datetime): Effective Datetime
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    if date:
        date = _strOrDate(date)
        return _get(
            "stock/{}/short-interest/{}".format(_quoteSymbols(symbol), date),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "stock/{}/short-interest".format(_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(shortInterest)
def shortInterestDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(shortInterest(*args, **kwargs)))

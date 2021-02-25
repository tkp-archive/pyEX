# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _expire, _get, _strOrDate, _toDatetime


@_expire(hour=8)
def calendar(
    type="holiday",
    direction="next",
    last=1,
    startDate=None,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This call allows you to fetch a number of trade dates or holidays from a given date. For example, if you want the next trading day, you would call /ref-data/us/dates/trade/next/1.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        type (str): "holiday" or "trade"
        direction (str): "next" or "last"
        last (int): number to move in direction
        startDate (date): start date for next or last, YYYYMMDD
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    if startDate:
        return _get(
            "ref-data/us/dates/{type}/{direction}/{last}/{date}".format(
                type=type, direction=direction, last=last, date=_strOrDate(startDate)
            ),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "ref-data/us/dates/" + type + "/" + direction + "/" + str(last),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(calendar)
def calendarDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(calendar(*args, **kwargs)))


@_expire(hour=8)
def holidays(
    direction="next",
    last=1,
    startDate=None,
    token="",
    version="stable",
    filter="",
    format="json",
):
    """This call allows you to fetch a number of trade dates or holidays from a given date. For example, if you want the next trading day, you would call /ref-data/us/dates/trade/next/1.

    https://iexcloud.io/docs/api/#u-s-exchanges
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        direction (str): "next" or "last"
        last (int): number to move in direction
        startDate (date): start date for next or last, YYYYMMDD
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return calendar(
        "holiday",
        direction,
        last,
        startDate,
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(holidays)
def holidaysDF(*args, **kwargs):
    return calendarDF(*args, **kwargs)

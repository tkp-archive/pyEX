# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from datetime import datetime
from functools import wraps

import pandas as pd

from ..common import PyEXception, _expire, _get, _reindex, _strOrDate, _toDatetime


def stats(token="", version="", filter="", format="json"):
    """https://iexcloud.io/docs/api/#stats-intraday

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get(
        "stats/intraday", token=token, version=version, filter=filter, format=format
    )


@wraps(stats)
def statsDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(stats(*args, **kwargs)))


def recent(token="", version="", filter="", format="json"):
    """https://iexcloud.io/docs/api/#stats-recent

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get(
        "stats/recent", token=token, version=version, filter=filter, format=format
    )


@wraps(recent)
def recentDF(*args, **kwargs):
    return _reindex(_toDatetime(pd.DataFrame(recent(*args, **kwargs))), "date")


def records(token="", version="", filter="", format="json"):
    """https://iexcloud.io/docs/api/#stats-records

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    return _get(
        "stats/records", token=token, version=version, filter=filter, format=format
    )


@wraps(records)
def recordsDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(records(*args, **kwargs)))


@_expire(hour=0)
def summary(date=None, token="", version="", filter="", format="json"):
    """https://iexcloud.io/docs/api/#stats-historical-summary

    Args:
        date (Optional[str]): Format YYYYMMDD date to fetch sentiment data. Default is today.
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    if date:
        if isinstance(date, str):
            return _get(
                "stats/historical?date=" + date,
                token=token,
                version=version,
                filter=filter,
                format=format,
            )
        elif isinstance(date, datetime):
            return _get(
                "stats/historical?date=" + date.strftime("%Y%m"),
                token=token,
                version=version,
                filter=filter,
                format=format,
            )
        else:
            raise PyEXception("Can't handle type : {}".format(str(type(date))))
    return _get(
        "stats/historical", token=token, version=version, filter=filter, format=format
    )


@wraps(summary)
def summaryDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(summary(*args, **kwargs)))


@_expire(hour=0)
def daily(date=None, last="", token="", version="", filter="", format="json"):
    """https://iexcloud.io/docs/api/#stats-historical-daily

    Args:
        date (Optional[str]): Format YYYYMMDD date to fetch sentiment data. Default is today.
        last (Optional[int]): Optional last number to include
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    if date:
        date = _strOrDate(date)
        return _get(
            "stats/historical/daily?date=" + date,
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    elif last:
        return _get(
            "stats/historical/daily?last=" + last,
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "stats/historical/daily",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(daily)
def dailyDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(daily(*args, **kwargs)))

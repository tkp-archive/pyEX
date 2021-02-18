# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd
from deprecation import deprecated

from ..common import _get, _strOrDate, _toDatetime


@deprecated(details="Deprecated: IEX Cloud status unkown")
def corporateActions(date=None, token="", version="", filter="", format="json"):
    """

    Args:
        date (datetime): Effective date
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
            "ref-data/daily-list/corporate-actions/" + date,
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "ref-data/daily-list/corporate-actions",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(corporateActions)
@deprecated(details="Deprecated: IEX Cloud status unkown")
def corporateActionsDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(corporateActions(*args, **kwargs)))


@deprecated(details="Deprecated: IEX Cloud status unkown")
def dividends(date=None, token="", version="", filter="", format="json"):
    """

    Args:
        date (datetime): Effective date
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
            "ref-data/daily-list/dividends/" + date,
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "ref-data/daily-list/dividends",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(dividends)
@deprecated(details="Deprecated: IEX Cloud status unkown")
def dividendsDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(dividends(*args, **kwargs)))


@deprecated(details="Deprecated: IEX Cloud status unkown")
def nextDayExtDate(date=None, token="", version="", filter="", format="json"):
    """

    Args:
        date (datetime): Effective date
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
            "ref-data/daily-list/next-day-ex-date/" + date,
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "ref-data/daily-list/next-day-ex-date",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(nextDayExtDate)
@deprecated(details="Deprecated: IEX Cloud status unkown")
def nextDayExtDateDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(nextDayExtDate(*args, **kwargs)))


@deprecated(details="Deprecated: IEX Cloud status unkown")
def directory(date=None, token="", version="", filter="", format="json"):
    """

    Args:
        date (datetime): Effective date
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
            "ref-data/daily-list/symbol-directory/" + date,
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "ref-data/daily-list/symbol-directory",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(directory)
@deprecated(details="Deprecated: IEX Cloud status unkown")
def directoryDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(directory(*args, **kwargs)))

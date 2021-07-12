# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

from ..common import (
    _UTC,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _reindex,
    _toDatetime,
    json_normalize,
)


@_expire(hour=4, tz=_UTC)
def company(symbol, token="", version="stable", filter="", format="json"):
    """Company reference data

    https://iexcloud.io/docs/api/#company
    Updates at 4am and 5am UTC every day

    Args:
        symbol (str): Ticker to request
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    return _get(
        "stock/{symbol}/company".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def _companyToDF(d):
    return _reindex(_toDatetime(json_normalize(d)), "symbol")


@wraps(company)
def companyDF(*args, **kwargs):
    return _companyToDF(company(*args, **kwargs))

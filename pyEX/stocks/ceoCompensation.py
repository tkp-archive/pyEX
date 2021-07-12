# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

from ..common import (
    _expire,
    _get,
    _raiseIfNotStr,
    _toDatetime,
    json_normalize,
)


@_expire(hour=1)
def ceoCompensation(symbol, token="", version="stable", filter="", format="json"):
    """This endpoint provides CEO compensation for a company by symbol.

    https://iexcloud.io/docs/api/#ceo-compensation
    1am daily

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
        "stock/{symbol}/ceo-compensation".format(symbol=symbol), token, version, filter
    )


@wraps(ceoCompensation)
def ceoCompensationDF(*args, **kwargs):
    return _toDatetime(json_normalize(ceoCompensation(*args, **kwargs)))

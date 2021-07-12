# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

from ..common import (
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _toDatetime,
    json_normalize,
)


def price(symbol, token="", version="stable", filter="", format="json"):
    """Price of ticker

    https://iexcloud.io/docs/api/#price
    4:30am-8pm ET Mon-Fri

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
        "stock/{symbol}/price".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(price)
def priceDF(*args, **kwargs):
    return _toDatetime(json_normalize({"price": price(*args, **kwargs)}))

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
    _toDatetime,
    json_normalize,
)


@_expire(hour=9, tz=_UTC)
def analystRecommendations(
    symbol, token="", version="stable", filter="", format="json"
):
    """Pulls data from the last four months.

    https://iexcloud.io/docs/api/#analyst-recommendations
    Updates at 9am, 11am, 12pm UTC every day

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
        "stock/{symbol}/recommendation-trends".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(analystRecommendations)
def analystRecommendationsDF(*args, **kwargs):
    return _toDatetime(json_normalize(analystRecommendations(*args, **kwargs)))

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
    _quoteSymbols,
    _raiseIfNotStr,
    _toDatetime,
)


@_expire(hour=5, tz=_UTC)
def insiderRoster(symbol, token="", version="stable", filter="", format="json"):
    """Returns the top 10 insiders, with the most recent information.

    https://iexcloud.io/docs/api/#insider-roster
    Updates at 5am, 6am ET every day

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
        "stock/{symbol}/insider-roster".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(insiderRoster)
def insiderRosterDF(*args, **kwargs):
    return _toDatetime(
        pd.DataFrame(insiderRoster(*args, **kwargs)), cols=[], tcols=["reportDate"]
    )

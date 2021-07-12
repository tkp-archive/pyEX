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

from ..common import (
    _UTC,
    _expire,
    _get,
    _quoteSymbols,
    _raiseIfNotStr,
    _toDatetime,
)


@_expire(hour=8, tz=_UTC)
@deprecated(details="Deprecated: IEX Cloud status unkown")
def relevant(symbol, token="", version="stable", filter="", format="json"):
    """Same as peers

    https://iexcloud.io/docs/api/#relevant
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
        "stock/{symbol}/relevant".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(relevant)
@deprecated(details="Deprecated: IEX Cloud status unkown")
def relevantDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(relevant(*args, **kwargs)))

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
    _reindex,
    _toDatetime,
)


@_expire(hour=8, tz=_UTC)
def peers(symbol, token="", version="stable", filter="", format="json"):
    """Peers of ticker

    https://iexcloud.io/docs/api/#peers
    8am UTC daily

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
        "stock/{symbol}/peers".format(symbol=_quoteSymbols(symbol)),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


def _peersToDF(d):
    df = _reindex(_toDatetime(pd.DataFrame(d, columns=["symbol"])), "symbol")
    df["peer"] = df.index
    return df


@wraps(peers)
def peersDF(*args, **kwargs):
    return _peersToDF(peers(*args, **kwargs))

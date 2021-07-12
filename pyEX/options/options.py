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

from ..common import _get, _raiseIfNotStr, _toDatetime, _timeseriesWrapper

from ..timeseries import timeSeries


def optionExpirations(symbol, token="", version="stable", filter="", format="json"):
    """Returns end of day options data

    https://iexcloud.io/docs/api/#options
    9:30am-5pm ET Mon-Fri

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
        "stock/" + symbol + "/options",
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@deprecated(details="Deprecated: Migrate to `options`")
def stockOptions(
    symbol,
    expiration,
    side="",
    token="",
    version="stable",
    filter="",
    format="json",
):
    """Returns end of day options data

    https://iexcloud.io/docs/api/#options
    9:30am-5pm ET Mon-Fri

    Args:
        symbol (str): Ticker to request
        expiration (str): Expiration date
        side (str): Side (optional)
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(symbol)
    if side:
        return _get(
            "stock/{symbol}/options/{expiration}/{side}".format(
                symbol=symbol, expiration=expiration, side=side
            ),
            token=token,
            version=version,
            filter=filter,
            format=format,
        )
    return _get(
        "stock/{symbol}/options/{expiration}/".format(
            symbol=symbol, expiration=expiration
        ),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(stockOptions)
def stockOptionsDF(*args, **kwargs):
    return _toDatetime(pd.DataFrame(stockOptions(*args, **kwargs)), tcols=["date"])


def options(
    contract, token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Options EOD prices
    Args:
        contract (str): Specific dated option contract, e.g. SPY20210714C00475000
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _raiseIfNotStr(contract)
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id=contract,
        key="chart",
        token=token,
        version=version,
        overrideBase="options",
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@wraps(options)
def optionsDF(*args, **kwargs):
    return _toDatetime(
        pd.DataFrame(options(*args, **kwargs)),
        reformatcols=["datetime", "date", "updated"],
    )

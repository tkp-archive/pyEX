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
)
from ..timeseries import timeSeries


@wraps(timeSeries)
@_expire(hour=8, tz=_UTC)
def tenQ(symbol, **kwargs):
    kwargs.pop("id", None)
    kwargs.pop("key", None)
    kwargs.pop("subkey", None)
    return timeSeries(id="REPORTED_FINANCIALS", key=symbol, subkey="10-Q", **kwargs)


@wraps(timeSeries)
@_expire(hour=8, tz=_UTC)
def tenK(symbol, **kwargs):
    kwargs.pop("id", None)
    kwargs.pop("key", None)
    kwargs.pop("subkey", None)
    return timeSeries(id="REPORTED_FINANCIALS", key=symbol, subkey="10-K", **kwargs)


@wraps(timeSeries)
@_expire(hour=8, tz=_UTC)
def twentyF(symbol, **kwargs):
    kwargs.pop("id", None)
    kwargs.pop("key", None)
    kwargs.pop("subkey", None)
    return timeSeries(id="REPORTED_FINANCIALS", key=symbol, subkey="20-F", **kwargs)


@wraps(timeSeries)
@_expire(hour=8, tz=_UTC)
def fortyF(symbol, **kwargs):
    kwargs.pop("id", None)
    kwargs.pop("key", None)
    kwargs.pop("subkey", None)
    return timeSeries(id="REPORTED_FINANCIALS", key=symbol, subkey="40-F", **kwargs)

# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

from ...common import _expire, _UTC
from ...timeseries import timeSeries, timeSeriesDF


@_expire(hour=11, tz=_UTC)
def _base(id, symbol="", **kwargs):
    """internal"""
    kwargs["id"] = id
    kwargs["key"] = symbol or kwargs.pop("key", "")
    return timeSeries(**kwargs)


@_expire(hour=11, tz=_UTC)
def _baseDF(id, symbol="", **kwargs):
    """internal"""
    kwargs["id"] = id
    kwargs["key"] = symbol or kwargs.pop("key", "")
    return timeSeriesDF(**kwargs)


@wraps(timeSeries)
def analystRecommendationsAndPriceTargetsInvisage(symbol="", **kwargs):
    """Current and historical Consensus Analyst Recommendations and Price Targets. Generated with Invisage’s proprietary smart consensus methodlogy.

    https://iexcloud.io/docs/api/#analyst-recommendations-and-price-targets-premium

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_INVISAGE_ESTIMATES", symbol=symbol, **kwargs)


@wraps(timeSeries)
def analystRecommendationsAndPriceTargetsInvisageDF(symbol="", **kwargs):
    """Current and historical Consensus Analyst Recommendations and Price Targets. Generated with Invisage’s proprietary smart consensus methodlogy.

    https://iexcloud.io/docs/api/#analyst-recommendations-and-price-targets-premium

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_INVISAGE_ESTIMATES", symbol=symbol, **kwargs)

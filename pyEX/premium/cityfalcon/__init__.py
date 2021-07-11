# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

from ...common import _interval
from ...timeseries import timeSeries, timeSeriesDF


@_interval(minutes=1)
def _base(id, symbol="", **kwargs):
    """internal"""
    kwargs["id"] = id
    kwargs["key"] = symbol or kwargs.pop("key", "")
    return timeSeries(**kwargs)


@_interval(minutes=1)
def _baseDF(id, symbol="", **kwargs):
    """internal"""
    kwargs["id"] = id
    kwargs["key"] = symbol or kwargs.pop("key", "")
    return timeSeriesDF(**kwargs)


@wraps(timeSeries)
def newsCityFalcon(symbol="", **kwargs):
    """CityFalcon democratises access to financial content and data, structures and personalises it, adds analytics, and delivers all of this in real-time. Covered are more than 300k financial and business topics, key people, organisations, stocks, sectors, locations, and more.
    Data is sourced from 10,000+ publications, encompassing a truly global view of markets and the events that affect them.
    Our natural language processing and machine learning models ensure relevancy for the chosen topics, and our in-house taxonomy offers more than simple keyword search, preventing false negatives when dealing with complex topics.

    https://iexcloud.io/docs/api/#cityfalcon-news

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _base(id="PREMIUM_CITYFALCON_NEWS", symbol=symbol, **kwargs)


@wraps(timeSeries)
def newsCityFalconDF(symbol="", **kwargs):
    """CityFalcon democratises access to financial content and data, structures and personalises it, adds analytics, and delivers all of this in real-time. Covered are more than 300k financial and business topics, key people, organisations, stocks, sectors, locations, and more.
    Data is sourced from 10,000+ publications, encompassing a truly global view of markets and the events that affect them.
    Our natural language processing and machine learning models ensure relevancy for the chosen topics, and our in-house taxonomy offers more than simple keyword search, preventing false negatives when dealing with complex topics.

    https://iexcloud.io/docs/api/#cityfalcon-news

    Args:
        symbol (str): symbol to use
        Supports all kwargs from `pyEX.timeseries.timeSeries`
    """
    return _baseDF(id="PREMIUM_CITYFALCON_NEWS", symbol=symbol, **kwargs)

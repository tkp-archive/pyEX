# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from enum import Enum
from functools import lru_cache, wraps

from ..common import _expire, _UTC, _timeseriesWrapper
from ..timeseries import timeSeries, timeSeriesDF, timeSeriesAsync


class CommoditiesPoints(Enum):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    Attributes:
        WTI; Crude oil West Texas Intermediate - in dollars per barrel, not seasonally adjusted
        BRENT; Crude oil Brent Europe - in dollars per barrel, not seasonally adjusted
        NATGAS; Henry Hub Natural Gas Spot Price - in dollars per million BTU, not seasonally adjusted
        HEATOIL; No. 2 Heating Oil New York Harbor - in dollars per gallon, not seasonally adjusted
        JET; Kerosense Type Jet Fuel US Gulf Coast - in dollars per gallon, not seasonally adjusted
        DIESEL; US Diesel Sales Price - in dollars per gallon, not seasonally adjusted
        GASREG; US Regular Conventional Gas Price - in dollars per gallon, not seasonally adjusted
        GASMID; US Midgrade Conventional Gas Price - in dollars per gallon, not seasonally adjusted
        GASPRM; US Premium Conventional Gas Price - in dollars per gallon, not seasonally adjusted
        PROPANE; Propane Prices Mont Belvieu Texas - in dollars per gallon, not seasonally adjusted
    """

    WTI = "DCOILWTICO"
    BRENT = "DCOILBRENTEU"
    NATGAS = "DHHNGSP"
    HEATOIL = "DHOILNYH"
    JET = "DJFUELUSGULF"
    DIESEL = "GASDESW"
    GASREG = "GASREGCOVW"
    GASMID = "GASMIDCOVW"
    GASPRM = "GASPRMCOVW"
    PROPANE = "DPROPANEMBTX"

    @staticmethod
    @lru_cache(1)
    def options():
        """Return a list of the available commodities points options"""
        return list(map(lambda c: c.value, CommoditiesPoints))


@_expire(hour=8, tz=_UTC)
def wti(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Commodities data

    https://iexcloud.io/docs/api/#commodities

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="ENERGY",
        key="DCOILWTICO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(wti)
def wtiDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ENERGY",
        key="DCOILWTICO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(wti)
async def wtiAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ENERGY",
        key="DCOILWTICO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def brent(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Commodities data

    https://iexcloud.io/docs/api/#commodities

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="ENERGY",
        key="DCOILBRENTEU",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(brent)
def brentDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ENERGY",
        key="DCOILBRENTEU",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(brent)
async def brentAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ENERGY",
        key="DCOILBRENTEU",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def natgas(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Commodities data

    https://iexcloud.io/docs/api/#commodities

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="ENERGY",
        key="DHHNGSP",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(natgas)
def natgasDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ENERGY",
        key="DHHNGSP",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(natgas)
async def natgasAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ENERGY",
        key="DHHNGSP",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def heatoil(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Commodities data

    https://iexcloud.io/docs/api/#commodities

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="ENERGY",
        key="DHOILNYH",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(heatoil)
def heatoilDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ENERGY",
        key="DHOILNYH",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(heatoil)
async def heatoilAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ENERGY",
        key="DHOILNYH",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def jet(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Commodities data

    https://iexcloud.io/docs/api/#commodities

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="ENERGY",
        key="DJFUELUSGULF",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(jet)
def jetDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ENERGY",
        key="DJFUELUSGULF",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(jet)
async def jetAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ENERGY",
        key="DJFUELUSGULF",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def diesel(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Commodities data

    https://iexcloud.io/docs/api/#commodities

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="ENERGY",
        key="GASDESW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(diesel)
def dieselDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ENERGY",
        key="GASDESW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(diesel)
async def dieselAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ENERGY",
        key="GASDESW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def gasreg(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Commodities data

    https://iexcloud.io/docs/api/#commodities

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="ENERGY",
        key="GASREGCOVW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(gasreg)
def gasregDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ENERGY",
        key="GASREGCOVW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(gasreg)
async def gasregAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ENERGY",
        key="GASREGCOVW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def gasmid(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Commodities data

    https://iexcloud.io/docs/api/#commodities

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="ENERGY",
        key="GASMIDCOVW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(gasmid)
def gasmidDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ENERGY",
        key="GASMIDCOVW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(gasmid)
async def gasmidAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesAsync(
        id="ENERGY",
        key="GASMIDCOVW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def gasprm(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Commodities data

    https://iexcloud.io/docs/api/#commodities

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="ENERGY",
        key="GASPRMCOVW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(gasprm)
def gasprmDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ENERGY",
        key="GASPRMCOVW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(gasprm)
async def gasprmAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ENERGY",
        key="GASPRMCOVW",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def propane(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Commodities data

    https://iexcloud.io/docs/api/#commodities

    Args:
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

        Supports all kwargs from `pyEX.timeseries.timeSeries`

    Returns:
        dict or DataFrame: result
    """
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeries(
        id="ENERGY",
        key="DPROPANEMBTX",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(propane)
def propaneDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ENERGY",
        key="DPROPANEMBTX",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(propane)
async def propaneAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ENERGY",
        key="DPROPANEMBTX",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )

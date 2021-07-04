# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from enum import Enum
from functools import lru_cache

from ..common import _expire, _UTC, _timeseriesWrapper
from ..points import points
from ..timeseries import timeSeries, timeSeriesDF


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
def wti(token="", version="stable"):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    WTI; Crude oil West Texas Intermediate - in dollars per barrel, not seasonally adjusted
    """
    return points("DCOILWTICO", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def wtiHistory(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def wtiHistoryDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def brent(token="", version="stable"):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    BRENT; Crude oil Brent Europe - in dollars per barrel, not seasonally adjusted
    """
    return points("DCOILBRENTEU", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def brentHistory(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def brentHistoryDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def natgas(token="", version="stable"):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    NATGAS; Henry Hub Natural Gas Spot Price - in dollars per million BTU, not seasonally adjusted
    """
    return points("DHHNGSP", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def natgasHistory(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def natgasHistoryDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def heatoil(token="", version="stable"):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    HEATOIL; No. 2 Heating Oil New York Harbor - in dollars per gallon, not seasonally adjusted
    """
    return points("DHOILNYH", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def heatoilHistory(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def heatoilHistoryDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def jet(token="", version="stable"):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    JET; Kerosense Type Jet Fuel US Gulf Coast - in dollars per gallon, not seasonally adjusted
    """
    return points("DJFUELUSGULF", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def jetHistory(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def jetHistoryDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def diesel(token="", version="stable"):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    DIESEL; US Diesel Sales Price - in dollars per gallon, not seasonally adjusted
    """
    return points("GASDESW", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def dieselHistory(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def dieselHistoryDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def gasreg(token="", version="stable"):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    GASREG; US Regular Conventional Gas Price - in dollars per gallon, not seasonally adjusted
    """
    return points("GASREGCOVW", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def gasregHistory(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def gasregHistoryDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def gasmid(token="", version="stable"):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    GASMID; US Midgrade Conventional Gas Price - in dollars per gallon, not seasonally adjusted
    """
    return points("GASMIDCOVW", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def gasmidHistory(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def gasmidHistoryDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def gasprm(token="", version="stable"):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    GASPRM; US Premium Conventional Gas Price - in dollars per gallon, not seasonally adjusted
    """
    return points("GASPRMCOVW", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def gasprmHistory(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def gasprmHistoryDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def propane(token="", version="stable"):
    """Commodities data points

    https://iexcloud.io/docs/api/#commodities

    PROPANE; Propane Prices Mont Belvieu Texas - in dollars per gallon, not seasonally adjusted
    """
    return points("DPROPANEMBTX", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def propaneHistory(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
def propaneHistoryDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
    return timeSeriesDF(
        id="ENERGY",
        key="DPROPANEMBTX",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )

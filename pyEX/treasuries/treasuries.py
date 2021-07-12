# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from enum import Enum
from functools import lru_cache

from ..common import _timeseriesWrapper, _expire, _UTC
from ..timeseries import timeSeries, timeSeriesDF


class TreasuriesPoints(Enum):
    """Treasury data points

    https://iexcloud.io/docs/api/#treasuries

    Attributes:
        THIRTY; 30 Year constant maturity rate
        TWENTY; 20 Year constant maturity rate
        TEN; 10 Year constant maturity rate
        FIVE; 5 Year constant maturity rate
        TWO; 2 Year constant maturity rate
        ONE; 1 Year constant maturity rate
        SIXMONTH; 6 Month constant maturity rate
        THREEMONTH; 3 Month constant maturity rate
        ONEMONTH; 1 Month constant maturity rate
    """

    THIRTY = "DGS30"
    TWENTY = "DGS20"
    TEN = "DGS10"
    SEVEN = "DGS7"
    FIVE = "DGS5"
    THREE = "DGS3"
    TWO = "DGS2"
    ONE = "DGS1"
    SIXMONTH = "DGS6MO"
    THREEMONTH = "DGS3MO"
    ONEMONTH = "DGS1MO"

    @staticmethod
    @lru_cache(1)
    def options():
        """Return a list of the available rates points options"""
        return list(map(lambda c: c.value, TreasuriesPoints))


@_expire(hour=8, tz=_UTC)
def thirtyYear(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS30",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def thirtyYearDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS30",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def twentyYear(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS20",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def twentyYearDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS20",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def tenYear(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS10",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def tenYearDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS10",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def sevenYear(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS7",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def sevenYearDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS7",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def fiveYear(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS5",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def fiveYearDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS5",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def threeYear(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS3",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def threeYearDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS3",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def twoYear(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS2",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def twoYearDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS2",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def oneYear(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS1",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def oneYearDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS1",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def sixMonth(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS6MO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def sixMonthDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS6MO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def threeMonth(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS3MO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def threeMonthDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS3MO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def oneMonth(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS1MO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def oneMonthDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    """Rates data

    https://iexcloud.io/docs/api/#treasuries

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
        id="TREASURY",
        key="DGS1MO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )

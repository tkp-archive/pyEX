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
from ..timeseries import timeSeries, timeSeriesDF


class MortgagePoints(Enum):
    """Mortgage data points

    https://iexcloud.io/docs/api/#mortgage-rates

    Attributes:
        US30; US 30-Year fixed rate mortgage average
        US15; US 15-Year fixed rate mortgage average
        US5; US 5/1-Year adjustable rate mortgage average
    """

    US30 = "MORTGAGE30US"
    US15 = "MORTGAGE15US"
    US5 = "MORTGAGE5US"

    @staticmethod
    @lru_cache(1)
    def options():
        """Return a list of the available economic points options"""
        return list(map(lambda c: c.value, MortgagePoints))


@_expire(hour=8, tz=_UTC)
def us30(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Economic data

    https://iexcloud.io/docs/api/#economic-data

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
        id="MORTGAGE",
        key="MORTGAGE30US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def us30DF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Economic data

    https://iexcloud.io/docs/api/#economic-data

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
        id="MORTGAGE",
        key="MORTGAGE30US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def us15(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Economic data

    https://iexcloud.io/docs/api/#economic-data

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
        id="MORTGAGE",
        key="MORTGAGE15US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def us15DF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Economic data

    https://iexcloud.io/docs/api/#economic-data

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
        id="MORTGAGE",
        key="MORTGAGE15US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def us5(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Economic data

    https://iexcloud.io/docs/api/#economic-data

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
        id="MORTGAGE",
        key="MORTGAGE5US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def us5DF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    """Economic data

    https://iexcloud.io/docs/api/#economic-data

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
        id="MORTGAGE",
        key="MORTGAGE5US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )

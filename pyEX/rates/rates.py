# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from enum import Enum
from functools import lru_cache

from ..common import _expire, _UTC, _timeseriesWrapper
from ..timeseries import timeSeries, timeSeriesDF


class RatesPoints(Enum):
    """Rates data points

    https://iexcloud.io/docs/api/#cd-rates
    https://iexcloud.io/docs/api/#credit-card-interest-rate

    Attributes:
        CREDITCARD; Commercial bank credit card interest rate as a percent, not seasonally adjusted
        CDNJ; CD Rate Non-Jumbo less than $100,000 Money market
        CDJ; CD Rate Jumbo more than $100,000 Money market
    """

    CREDITCARD = "TERMCBCCALLNS"
    CDNJ = "MMNRNJ"
    CDJ = "MMNRJD"

    @staticmethod
    @lru_cache(1)
    def options():
        """Return a list of the available economic points options"""
        return list(map(lambda c: c.value, RatesPoints))


@_expire(hour=8, tz=_UTC)
def creditcard(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
        id="RATES",
        key="TERMCBCCALLNS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def creditcardDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
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
        id="RATES",
        key="TERMCBCCALLNS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def cdnj(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="RATES",
        key="MMNRNJ",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def cdnjDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="RATES",
        key="MMNRNJ",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def cdj(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="RATES",
        key="MMNRJD",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def cdjDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="RATES",
        key="MMNRJD",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )

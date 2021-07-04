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
from ..points import points
from ..timeseries import timeSeries, timeSeriesDF


class RatesPoints(Enum):
    """Rates data points

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
        return list(map(lambda c: c.value, RatesPoints))


@_expire(hour=8, tz=_UTC)
def thirtyYear(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    THIRTY; 30 Year constant maturity rate
    """
    return points("DGS30", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def thirtyYearHistory(
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
def thirtyYearHistoryDF(
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
def twentyYear(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    TWENTY; 20 Year constant maturity rate
    """
    return points("DGS20", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def twentyYearHistory(
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
def twentyYearHistoryDF(
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
def tenYear(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    TEN; 10 Year constant maturity rate
    """
    return points("DGS10", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def tenYearHistory(
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
        key="DGS10",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def tenYearHistoryDF(
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
def sevenYear(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    SEVEN; 7 Year constant maturity rate
    """
    return points("DGS7", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def sevenYearHistory(
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
def sevenYearHistoryDF(
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
def fiveYear(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    FIVE; 5 Year constant maturity rate
    """
    return points("DGS5", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def fiveYearHistory(
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
        key="DGS5",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def fiveYearHistoryDF(
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
def threeYear(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    THREE; 3 Year constant maturity rate
    """
    return points("DGS3", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def threeYearHistory(
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
def threeYearHistoryDF(
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
def twoYear(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    TWO; 2 Year constant maturity rate
    """
    return points("DGS2", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def twoYearHistory(
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
        key="DGS2",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def twoYearHistoryDF(
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
def oneYear(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    ONE; 1 Year constant maturity rate
    """
    return points("DGS1", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def oneYearHistory(
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
        key="DGS1",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def oneYearHistoryDF(
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
def sixMonth(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    SIXMONTH; 6 Month constant maturity rate
    """
    return points("DGS6MO", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def sixMonthHistory(
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
        key="DGS6MO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def sixMonthHistoryDF(
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
def threeMonth(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    THREEMONTH; 3 Month constant maturity rate
    """
    return points("DGS3MO", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def threeMonthHistory(
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
def threeMonthHistoryDF(
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
def oneMonth(token="", version="stable"):
    """Rates data points

    https://iexcloud.io/docs/api/#treasuries

    ONEMONTH; 1 Month constant maturity rate
    """
    return points("DGS1MO", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def oneMonthHistory(
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
        key="DGS1MO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def oneMonthHistoryDF(
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

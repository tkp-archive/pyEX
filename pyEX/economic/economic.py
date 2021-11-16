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


class EconomicPoints(Enum):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    Attributes:
        FEDFUNDS; Effective federal funds rate
        GDP; Real Gross Domestic Product
        INDPRO; Industrial Production Index
        CPI; Consumer Price Index All Urban Consumers
        PAYROLL; Total nonfarm employees in thousands of persons seasonally adjusted
        HOUSING; Total Housing Starts in thousands of units, seasonally adjusted annual rate
        UNEMPLOYMENT; Unemployment rate returned as a percent, seasonally adjusted
        VEHICLES; Total Vehicle Sales in millions of units
        RECESSION; US Recession Probabilities. Smoothed recession probabilities for the United States are obtained from a dynamic-factor markov-switching model applied to four monthly coincident variables. non-farm payroll employment, the index of industrial production, real personal income excluding transfer payments, and real manufacturing and trade sales.
        INITIALCLAIMS; Initial claims returned as a number, seasonally adjusted
        RETAILMONEY; Retail money funds returned as billions of dollars, seasonally adjusted
        INSTITUTIONALMONEY; Institutional money funds returned as billions of dollars, seasonally adjusted
    """

    FEDFUNDS = "FEDFUNDS"
    GDP = "A191RL1Q225SBEA"
    INDPRO = "INDPRO"
    CPI = "CPIAUCSL"
    PAYROLL = "PAYEMS"
    HOUSING = "HOUST"
    UNEMPLOYMENT = "UNRATE"
    VEHICLES = "TOTALSA"
    RECESSION_PROB = "RECPROUSM156N"
    INITIALCLAIMS = "IC4WSA"
    RETAILMONEY = "WRMFSL"
    INSTITUTIONALMONEY = "WIMFSL"

    @staticmethod
    @lru_cache(1)
    def options():
        """Return a list of the available economic points options"""
        return list(map(lambda c: c.value, EconomicPoints))


@_expire(hour=8, tz=_UTC)
def fedfunds(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="ECONOMIC",
        key="FEDFUNDS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(fedfunds)
def fedfundsDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="FEDFUNDS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(fedfunds)
async def fedfundsAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="FEDFUNDS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def gdp(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="ECONOMIC",
        key="A191RL1Q225SBEA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(gdp)
def gdpDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="A191RL1Q225SBEA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(gdp)
async def gdpAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="A191RL1Q225SBEA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def indpro(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="ECONOMIC",
        key="INDPRO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(indpro)
def indproDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="INDPRO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(indpro)
async def indproAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="INDPRO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def cpi(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="ECONOMIC",
        key="CPIAUCSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(cpi)
def cpiDF(token="", version="stable", filter="", format="json", **timeseries_kwargs):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="CPIAUCSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(cpi)
async def cpiAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="CPIAUCSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def payroll(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="ECONOMIC",
        key="PAYEMS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(payroll)
def payrollDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="PAYEMS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(payroll)
async def payrollAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="PAYEMS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def housing(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="ECONOMIC",
        key="HOUST",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(housing)
def housingDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="HOUST",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(housing)
async def housingAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="HOUST",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def unemployment(
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
        id="ECONOMIC",
        key="UNRATE",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(unemployment)
def unemploymentDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="UNRATE",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(unemployment)
async def unemploymentAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="UNRATE",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def vehicles(token="", version="stable", filter="", format="json", **timeseries_kwargs):
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
        id="ECONOMIC",
        key="TOTALSA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(vehicles)
def vehiclesDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="TOTALSA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(vehicles)
async def vehiclesAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="TOTALSA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def recessionProb(
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
        id="ECONOMIC",
        key="RECPROUSM156N",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(recessionProb)
def recessionProbDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="RECPROUSM156N",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(recessionProb)
async def recessionProbAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="RECPROUSM156N",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def initialClaims(
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
        id="ECONOMIC",
        key="IC4WSA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(initialClaims)
def initialClaimsDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="IC4WSA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(initialClaims)
async def initialClaimsAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="IC4WSA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def institutionalMoney(
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
        id="ECONOMIC",
        key="WRMFSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(institutionalMoney)
def institutionalMoneyDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="WRMFSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(institutionalMoney)
async def institutionalMoneyAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="WRMFSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def retailMoney(
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
        id="ECONOMIC",
        key="WIMFSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(retailMoney)
def retailMoneyDF(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return timeSeriesDF(
        id="ECONOMIC",
        key="WIMFSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
@wraps(retailMoney)
async def retailMoneyAsync(
    token="", version="stable", filter="", format="json", **timeseries_kwargs
):
    _timeseriesWrapper(timeseries_kwargs)
    return await timeSeriesAsync(
        id="ECONOMIC",
        key="WIMFSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )

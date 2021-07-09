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


class EconomicPoints(Enum):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    Attributes:
        US0; US 30-Year fixed rate mortgage average
        US5; US 15-Year fixed rate mortgage average
        US; US 5/1-Year adjustable rate mortgage average
        FEDFUNDS; Effective federal funds rate
        CREDITCARD; Commercial bank credit card interest rate as a percent, not seasonally adjusted
        CDNJ; CD Rate Non-Jumbo less than $100,000 Money market
        CDJ; CD Rate Jumbo more than $100,000 Money market
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

    US30 = "MORTGAGE30US"
    US15 = "MORTGAGE15US"
    US5 = "MORTGAGE5US"
    FEDFUNDS = "FEDFUNDS"
    CREDITCARD = "TERMCBCCALLNS"
    CDNJ = "MMNRNJ"
    CDJ = "MMNRJD"
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
def us30(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    US0; US 30-Year fixed rate mortgage average
    """
    return points("MORTGAGE30US", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def us30History(
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
        id="MORTGAGE",
        key="MORTGAGE30US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def us30HistoryDF(
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
        id="MORTGAGE",
        key="MORTGAGE30US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def us15(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    US5; US 15-Year fixed rate mortgage average
    """
    return points("MORTGAGE15US", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def us15History(
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
        id="MORTGAGE",
        key="MORTGAGE15US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def us15HistoryDF(
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
        id="MORTGAGE",
        key="MORTGAGE15US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def us5(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    US; US 5/1-Year adjustable rate mortgage average
    """
    return points("MORTGAGE5US", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def us5History(
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
        id="MORTGAGE",
        key="MORTGAGE5US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def us5HistoryDF(
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
        id="MORTGAGE",
        key="MORTGAGE5US",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def fedfunds(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    FEDFUNDS; Effective federal funds rate
    """
    return points("FEDFUNDS", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def fedfundsHistory(
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
        key="FEDFUNDS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def fedfundsHistoryDF(
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
        id="ECONOMIC",
        key="FEDFUNDS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def creditcard(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    CREDITCARD; Commercial bank credit card interest rate as a percent, not seasonally adjusted
    """
    return points("TERMCBCCALLNS", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def creditcardHistory(
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
def creditcardHistoryDF(
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
def cdnj(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    CDNJ; CD Rate Non-Jumbo less than $100,000 Money market
    """
    return points("MMNRNJ", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def cdnjHistory(
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
        key="MMNRNJ",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def cdnjHistoryDF(
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
        key="MMNRNJ",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def cdj(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    CDJ; CD Rate Jumbo more than $100,000 Money market
    """
    return points("MMNRJD", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def cdjHistory(
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
        key="MMNRJD",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def cdjHistoryDF(
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
        key="MMNRJD",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def gdp(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    GDP; Real Gross Domestic Product
    """
    return points("A191RL1Q225SBEA", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def gdpHistory(
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
        key="A191RL1Q225SBEA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def gdpHistoryDF(
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
        id="ECONOMIC",
        key="A191RL1Q225SBEA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def indpro(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    INDPRO; Industrial Production Index
    """
    return points("INDPRO", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def indproHistory(
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
        key="INDPRO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def indproHistoryDF(
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
        id="ECONOMIC",
        key="INDPRO",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def cpi(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    CPI; Consumer Price Index All Urban Consumers
    """
    return points("CPIAUCSL", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def cpiHistory(
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
        key="CPIAUCSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def cpiHistoryDF(
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
        id="ECONOMIC",
        key="CPIAUCSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def payroll(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    PAYROLL; Total nonfarm employees in thousands of persons seasonally adjusted
    """
    return points("PAYEMS", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def payrollHistory(
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
        key="PAYEMS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def payrollHistoryDF(
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
        id="ECONOMIC",
        key="PAYEMS",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def housing(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    HOUSING; Total Housing Starts in thousands of units, seasonally adjusted annual rate
    """
    return points("HOUST", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def housingHistory(
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
        key="HOUST",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def housingHistoryDF(
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
        id="ECONOMIC",
        key="HOUST",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def unemployment(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    UNEMPLOYMENT; Unemployment rate returned as a percent, seasonally adjusted
    """
    return points("UNRATE", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def unemploymentHistory(
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
def unemploymentHistoryDF(
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
        id="ECONOMIC",
        key="UNRATE",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def vehicles(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    VEHICLES; Total Vehicle Sales in millions of units
    """
    return points("TOTALSA", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def vehiclesHistory(
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
        key="TOTALSA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def vehiclesHistoryDF(
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
        id="ECONOMIC",
        key="TOTALSA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def recessionProb(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    RECESSION; US Recession Probabilities. Smoothed recession probabilities for the United States are obtained from a dynamic-factor markov-switching model applied to four monthly coincident variables. non-farm payroll employment, the index of industrial production, real personal income excluding transfer payments, and real manufacturing and trade sales.
    """
    return points("RECPROUSM156N", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def recessionProbHistory(
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
def recessionProbHistoryDF(
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
        id="ECONOMIC",
        key="RECPROUSM156N",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def initialClaims(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    INITIALCLAIMS; Initial claims returned as a number, seasonally adjusted
    """
    return points("IC4WSA", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def initialClaimsHistory(
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
def initialClaimsHistoryDF(
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
        id="ECONOMIC",
        key="IC4WSA",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def institutionalMoney(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    INSTITUTIONALMONEY; Institutional money funds returned as billions of dollars, seasonally adjusted
    """
    return points("WRMFSL", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def institutionalMoneyHistory(
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
def institutionalMoneyHistoryDF(
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
        id="ECONOMIC",
        key="WRMFSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )


@_expire(hour=8, tz=_UTC)
def retailMoney(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    RETAILMONEY; Retail money funds returned as billions of dollars, seasonally adjusted
    """
    return points("WIMFSL", token=token, version=version)


@_expire(hour=8, tz=_UTC)
def retailMoneyHistory(
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
def retailMoneyHistoryDF(
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
        id="ECONOMIC",
        key="WIMFSL",
        token=token,
        version=version,
        filter=filter,
        format=format,
        **timeseries_kwargs
    )

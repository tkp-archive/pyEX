# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from enum import Enum
from functools import lru_cache

from ..points import points


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


def us30(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    US0; US 30-Year fixed rate mortgage average
    """
    return points("MORTGAGE30US", token=token, version=version)


def us15(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    US5; US 15-Year fixed rate mortgage average
    """
    return points("MORTGAGE15US", token=token, version=version)


def us5(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    US; US 5/1-Year adjustable rate mortgage average
    """
    return points("MORTGAGE5US", token=token, version=version)


def fedfunds(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    FEDFUNDS; Effective federal funds rate
    """
    return points("FEDFUNDS", token=token, version=version)


def creditcard(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    CREDITCARD; Commercial bank credit card interest rate as a percent, not seasonally adjusted
    """
    return points("TERMCBCCALLNS", token=token, version=version)


def cdnj(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    CDNJ; CD Rate Non-Jumbo less than $100,000 Money market
    """
    return points("MMNRNJ", token=token, version=version)


def cdj(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    CDJ; CD Rate Jumbo more than $100,000 Money market
    """
    return points("MMNRJD", token=token, version=version)


def gdp(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    GDP; Real Gross Domestic Product
    """
    return points("A191RL1Q225SBEA", token=token, version=version)


def indpro(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    INDPRO; Industrial Production Index
    """
    return points("INDPRO", token=token, version=version)


def cpi(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    CPI; Consumer Price Index All Urban Consumers
    """
    return points("CPIAUCSL", token=token, version=version)


def payroll(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    PAYROLL; Total nonfarm employees in thousands of persons seasonally adjusted
    """
    return points("PAYEMS", token=token, version=version)


def housing(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    HOUSING; Total Housing Starts in thousands of units, seasonally adjusted annual rate
    """
    return points("HOUST", token=token, version=version)


def unemployment(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    UNEMPLOYMENT; Unemployment rate returned as a percent, seasonally adjusted
    """
    return points("UNRATE", token=token, version=version)


def vehicles(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    VEHICLES; Total Vehicle Sales in millions of units
    """
    return points("TOTALSA", token=token, version=version)


def recessionProb(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    RECESSION; US Recession Probabilities. Smoothed recession probabilities for the United States are obtained from a dynamic-factor markov-switching model applied to four monthly coincident variables. non-farm payroll employment, the index of industrial production, real personal income excluding transfer payments, and real manufacturing and trade sales.
    """
    return points("RECPROUSM156N", token=token, version=version)


def initialClaims(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    INITIALCLAIMS; Initial claims returned as a number, seasonally adjusted
    """
    return points("IC4WSA", token=token, version=version)


def institutionalMoney(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    INSTITUTIONALMONEY; Institutional money funds returned as billions of dollars, seasonally adjusted
    """
    return points("WRMFSL", token=token, version=version)


def retailMoney(token="", version="stable"):
    """Economic data points

    https://iexcloud.io/docs/api/#economic-data

    RETAILMONEY; Retail money funds returned as billions of dollars, seasonally adjusted
    """
    return points("WIMFSL", token=token, version=version)

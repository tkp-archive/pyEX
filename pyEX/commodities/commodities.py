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


def wti(token="", version="stable"):
    return points("DCOILWTICO", token=token, version=version)


def brent(token="", version="stable"):
    return points("DCOILBRENTEU", token=token, version=version)


def natgas(token="", version="stable"):
    return points("DHHNGSP", token=token, version=version)


def heatoil(token="", version="stable"):
    return points("DHOILNYH", token=token, version=version)


def jet(token="", version="stable"):
    return points("DJFUELUSGULF", token=token, version=version)


def diesel(token="", version="stable"):
    return points("GASDESW", token=token, version=version)


def gasreg(token="", version="stable"):
    return points("GASREGCOVW", token=token, version=version)


def gasmid(token="", version="stable"):
    return points("GASMIDCOVW", token=token, version=version)


def gasprm(token="", version="stable"):
    return points("GASPRMCOVW", token=token, version=version)


def propane(token="", version="stable"):
    return points("DPROPANEMBTX", token=token, version=version)

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
    FIVE = "DGS5"
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


def thirtyYear(token="", version="stable"):
    return points("DGS30", token=token, version=version)


def twentyYear(token="", version="stable"):
    return points("DGS20", token=token, version=version)


def tenYear(token="", version="stable"):
    return points("DGS10", token=token, version=version)


def fiveYear(token="", version="stable"):
    return points("DGS5", token=token, version=version)


def twoYear(token="", version="stable"):
    return points("DGS2", token=token, version=version)


def oneYear(token="", version="stable"):
    return points("DGS1", token=token, version=version)


def sixMonth(token="", version="stable"):
    return points("DGS6MO", token=token, version=version)


def threeMonth(token="", version="stable"):
    return points("DGS3MO", token=token, version=version)


def oneMonth(token="", version="stable"):
    return points("DGS1MO", token=token, version=version)

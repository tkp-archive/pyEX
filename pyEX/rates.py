from enum import Enum
from functools import lru_cache


class RatesPoints(Enum):
    THIRTY = 'DGS30'
    TWENTY = 'DGS20'
    TEN = 'DGS10'
    FIVE = 'DGS5'
    TWO = 'DGS2'
    ONE = 'DGS1'
    SIXMONTH = 'DGS6MO'
    THREEMONTH = 'DGS3MO'
    ONEMONTH = 'DGS1MO'

    @staticmethod
    @lru_cache(1)
    def options():
        return list(map(lambda c: c.value, RatesPoints))

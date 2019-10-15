from enum import Enum


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
    def options():
        return list(map(lambda c: c.value, RatesPoints))

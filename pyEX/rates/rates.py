from enum import Enum
from functools import lru_cache


class RatesPoints(Enum):
    '''Rates data points

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
    '''
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
        '''Return a list of the available rates points options'''
        return list(map(lambda c: c.value, RatesPoints))

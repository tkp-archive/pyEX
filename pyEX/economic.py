from enum import Enum
from functools import lru_cache


class EconomicPoints(Enum):
    US30 = 'MORTGAGE30US'
    US15 = 'MORTGAGE15US'
    US5 = 'MORTGAGE5US'
    FEDFUNDS = 'FEDFUNDS'
    CREDITCARD = 'TERMCBCCALLNS'
    CDNJ = 'MMNRNJ'
    CDJ = 'MMNRJD'
    GDP = 'A191RL1Q225SBEA'
    INDPRO = 'INDPRO'
    CPI = 'CPIAUCSL'
    PAYROLL = 'PAYEMS'
    HOUSING = 'HOUST'
    UNEMPLOYMENT = 'UNRATE'
    VEHICLES = 'TOTALSA'
    RECESSION_PROB = 'RECPROUSM156N'

    @staticmethod
    @lru_cache(1)
    def options():
        return list(map(lambda c: c.value, EconomicPoints))

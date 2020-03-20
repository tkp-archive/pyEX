from enum import Enum
from functools import lru_cache


class EconomicPoints(Enum):
    '''Economic data points

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
    '''

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
    INITIALCLAIMS = 'IC4WSA'
    RETAILMONEY = 'WRMFSL'
    INSTITUTIONALMONEY = 'WIMFSL'

    @staticmethod
    @lru_cache(1)
    def options():
        '''Return a list of the available economic points options'''
        return list(map(lambda c: c.value, EconomicPoints))

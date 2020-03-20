from functools import lru_cache
from enum import Enum


class CommoditiesPoints(Enum):
    '''Commodities data points

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
    '''
    WTI = 'DCOILWTICO'
    BRENT = 'DCOILBRENTEU'
    NATGAS = 'DHHNGSP'
    HEATOIL = 'DHOILNYH'
    JET = 'DJFUELUSGULF'
    DIESEL = 'GASDESW'
    GASREG = 'GASREGCOVW'
    GASMID = 'GASMIDCOVW'
    GASPRM = 'GASPRMCOVW'
    PROPANE = 'DPROPANEMBTX'

    @staticmethod
    @lru_cache(1)
    def options():
        '''Return a list of the available commodities points options'''
        return list(map(lambda c: c.value, CommoditiesPoints))

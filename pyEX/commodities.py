from functools import lru_cache
from enum import Enum


class CommoditiesPoints(Enum):
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
        return list(map(lambda c: c.value, CommoditiesPoints))

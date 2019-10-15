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
    def options():
        return list(map(lambda c: c.value, CommoditiesPoints))

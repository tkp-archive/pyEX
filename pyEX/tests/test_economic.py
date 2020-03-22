# for Coverage
from mock import patch


class TestEconomic:
    def test_all(self):
        from pyEX import Client
        c = Client('test')
        with patch('pyEX.common._getJsonIEXCloud'), \
                patch('pickle.dump'):
            c.us30()
            c.us15()
            c.us5()
            c.fedfunds()
            c.creditcard()
            c.cdnj()
            c.cdj()
            c.gdp()
            c.indpro()
            c.cpi()
            c.payroll()
            c.housing()
            c.unemployment()
            c.vehicles()
            c.recessionProb()
            c.initialClaims()
            c.institutionalMoney()
            c.retailMoney()

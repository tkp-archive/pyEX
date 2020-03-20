# for Coverage
from mock import patch


class TestCommodities:
    def test_all(self):
        from pyEX import Client
        c = Client('test')
        with patch('pyEX.common._getJsonIEXCloud'), \
                patch('pickle.dump'):
            c.wti()
            c.brent()
            c.natgas()
            c.heatoil()
            c.jet()
            c.diesel()
            c.gasreg()
            c.gasmid()
            c.gasprm()
            c.propane()

# for Coverage
from mock import patch


class TestRates:
    def test_all(self):
        from pyEX import Client
        c = Client('test')
        with patch('pyEX.common._getJsonIEXCloud'), \
                patch('pickle.dump'):
            c.thirtyYear()
            c.twentyYear()
            c.tenYear()
            c.fiveYear()
            c.twoYear()
            c.oneYear()
            c.sixMonth()
            c.threeMonth()
            c.oneMonth()

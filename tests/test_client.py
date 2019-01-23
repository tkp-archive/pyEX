# for Coverage
from mock import patch, MagicMock
C = 'AAPL'


class TestClient:
    def test_client(self):
        from pyEX import Client
        c = Client('test')

    def test_account(self):
        from pyEX import Client
        c = Client('test')
        with patch('pyEX.client._getJson'):
            c.account()

    def test_usage(self):
        from pyEX import Client
        from pyEX import PyEXception
        c = Client('test')
        with patch('pyEX.client._getJson'):
            c.usage()
            c.usage('messages')
            try:
                c.usage('test')
                assert False
            except PyEXception:
                pass

# for Coverage
from mock import patch, MagicMock
C = 'AAPL'


class TestClient:
    def test_client(self):
        from pyEX import Client
        c = Client('test')

    def test_client_notoken(self):
        import os
        from pyEX import Client, PyEXception
        tmp = os.environ.pop('IEX_TOKEN', '')
        try:
            Client()
            assert False
        except PyEXception:
            pass
        os.environ['IEX_TOKEN'] = tmp

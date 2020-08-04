# for Coverage
from mock import patch, MagicMock
SYMBOL = 'aapl'


class TestAll:
    def test_other(self):
        from pyEX.marketdata.sse import _runSSE, DeepChannelsSSE
        with patch('pyEX.marketdata.sse._streamSSE'):
            # coverage
            _runSSE('test')
            _runSSE('test', symbols=['test'])

            # coverage
            DeepChannelsSSE.options()

    def test_tops(self):
        from pyEX import Client
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            c = Client(version='sandbox')

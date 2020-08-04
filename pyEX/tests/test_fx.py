# for Coverage
import time
from mock import patch, MagicMock
SYMBOL = 'usdjpy'


class TestAll:
    def teardown(self):
        time.sleep(.1)  # prevent being blocked

    def test_latestfx(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.latestFXDF()
            c.latestFXDF(SYMBOL)

    def test_convertfx(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.convertFXDF()
            c.convertFXDF(SYMBOL)
            c.convertFXDF(SYMBOL, amount=1.0)

    def test_historicalfx(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.historicalFXDF()
            c.historicalFXDF(SYMBOL)

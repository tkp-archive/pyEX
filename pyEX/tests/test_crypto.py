# for Coverage
import time
from mock import patch, MagicMock
SYMBOL = 'BTCUSD'


class TestAll:
    def teardown(self):
        time.sleep(.1)  # prevent being blocked

    def test_bookcrypto(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.cryptoBookDF(SYMBOL)

    def test_pricecrypto(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.cryptoPriceDF(SYMBOL)

    def test_quotecrypto(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.cryptoQuoteDF(SYMBOL)

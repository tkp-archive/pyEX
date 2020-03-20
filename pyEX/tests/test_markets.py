# for Coverage
from mock import patch, MagicMock


class TestAll:
    def test_markets(self):
        from pyEX import markets
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            markets()

    def test_marketsDF(self):
        from pyEX import marketsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            marketsDF()

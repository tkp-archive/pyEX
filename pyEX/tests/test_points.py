# for Coverage
import time
from mock import patch, MagicMock
SYMBOL = 'aapl'


class TestPoints:
    def teardown(self):
        time.sleep(.1)  # prevent being blocked

    def test_points(self):
        from pyEX import points
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            points()
            points('aapl')
            points('aapl', 'test')

    def test_pointsDF(self):
        from pyEX import pointsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            pointsDF('test')

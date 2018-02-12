# for Coverage
from mock import patch, MagicMock


class TestAll:
    def setup(self):
        pass
        # setup() before each test method

    def teardown(self):
        pass
        # teardown() after each test method

    @classmethod
    def setup_class(cls):
        pass
        # setup_class() before any methods in this class

    @classmethod
    def teardown_class(cls):
        pass
        # teardown_class() after any methods in this class

    def test_tops(self):
        from pyEX import tops
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            tops()
            tops('test')
            tops(['test'])

    def test_last(self):
        from pyEX import last
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            last()
            last('test')

    def test_hist(self):
        from datetime import datetime
        from pyEX import hist
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            hist()
            hist('201505')
            hist(datetime.today())

    def test_deep(self):
        from pyEX import deep
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            deep()
            deep('test')

    def test_book(self):
        from pyEX import topsBook
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            topsBook()
            topsBook('test')

    def test_trades(self):
        from pyEX import trades
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            trades()
            trades('test')

    def test_systemEvent(self):
        from pyEX import systemEvent
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            systemEvent()

    def test_tradingStatus(self):
        from pyEX import tradingStatus
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            tradingStatus()
            tradingStatus('test')

    def test_opHaltStatus(self):
        from pyEX import opHaltStatus
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            opHaltStatus()
            opHaltStatus('test')

    def test_ssrStatus(self):
        from pyEX import ssrStatus
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            ssrStatus()
            ssrStatus('test')

    def test_securityEvent(self):
        from pyEX import securityEvent
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            securityEvent()
            securityEvent('test')

    def test_tradeBreak(self):
        from pyEX import tradeBreak
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            tradeBreak()
            tradeBreak('test')

    def test_auction(self):
        from pyEX import auction
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            auction()
            auction('test')

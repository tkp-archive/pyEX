# for Coverage
from mock import patch, MagicMock
SYMBOL = 'aapl'


class TestAll:
    def test_tops(self):
        from pyEX import tops
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            tops()
            tops('test')
            tops(['test'])

    def test_topsDF(self):
        from pyEX import topsDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            topsDF()

    def test_last(self):
        from pyEX import last
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            last()
            last('test')

    def test_lastDF(self):
        from pyEX import lastDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            lastDF()

    def test_hist(self):
        from datetime import datetime
        from pyEX import hist
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            hist()
            hist('201505')
            hist(datetime.today())

    def test_histDF(self):
        from pyEX import histDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            histDF()

    def test_deep(self):
        from pyEX import deep
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            deep()
            deep('test')

    def test_deepDF(self):
        from pyEX import deepDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            deepDF()
            deepDF('test')

    def test_book(self):
        from pyEX import deepBook
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            deepBook()
            deepBook('test')

    def test_bookDF(self):
        from pyEX import deepBookDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            deepBookDF()
            deepBookDF('test')

    def test_trades(self):
        from pyEX import trades
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            trades()
            trades('test')

    def test_tradesDF(self):
        from pyEX import tradesDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            tradesDF()
            tradesDF('test')

    def test_systemEvent(self):
        from pyEX import systemEvent
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            systemEvent()

    def test_systemEventDF(self):
        from pyEX import systemEventDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            systemEventDF()

    def test_tradingStatus(self):
        from pyEX import tradingStatus
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            tradingStatus()
            tradingStatus('test')

    def test_tradingStatusDF(self):
        from pyEX import tradingStatusDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            tradingStatusDF()
            tradingStatusDF('test')

    def test_opHaltStatus(self):
        from pyEX import opHaltStatus
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            opHaltStatus()
            opHaltStatus('test')

    def test_opHaltStatusDF(self):
        from pyEX import opHaltStatusDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            opHaltStatusDF()
            opHaltStatusDF('test')

    def test_ssrStatus(self):
        from pyEX import ssrStatus
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            ssrStatus()
            ssrStatus('test')

    def test_ssrStatusDF(self):
        from pyEX import ssrStatusDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            ssrStatusDF()
            ssrStatusDF('test')

    def test_securityEvent(self):
        from pyEX import securityEvent
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            securityEvent()
            securityEvent('test')

    def test_securityEventDF(self):
        from pyEX import securityEventDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            securityEventDF()
            securityEventDF('test')

    def test_tradeBreak(self):
        from pyEX import tradeBreak
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            tradeBreak()
            tradeBreak('test')

    def test_tradeBreakDF(self):
        from pyEX import tradeBreakDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            tradeBreakDF()
            tradeBreakDF('test')

    def test_auction(self):
        from pyEX import auction
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            auction()
            auction('test')

    def test_auctionDF(self):
        from pyEX import auctionDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            auctionDF()
            auctionDF('test')

    def test_officialPrice(self):
        from pyEX import officialPrice
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            officialPrice()
            officialPrice('test')

    def test_officialPriceDF(self):
        from pyEX import officialPriceDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            officialPriceDF()
            officialPriceDF('test')

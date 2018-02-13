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
        from pyEX import topsWS
        with patch('pyEX.marketdata.ws._stream'):
            topsWS()
            topsWS('test')
            topsWS(['test'])

    def test_last(self):
        from pyEX import lastWS
        with patch('pyEX.marketdata.ws._stream'):
            lastWS()
            lastWS('test')

    def test_deep(self):
        from pyEX import deepWS
        with patch('pyEX.marketdata.ws._stream'):
            deepWS()
            deepWS('test')

    def test_book(self):
        from pyEX import bookWS
        with patch('pyEX.marketdata.ws._stream'):
            bookWS()
            bookWS('test')

    def test_trades(self):
        from pyEX import tradesWS
        with patch('pyEX.marketdata.ws._stream'):
            tradesWS()
            tradesWS('test')

    def test_systemEvent(self):
        from pyEX import systemEventWS
        with patch('pyEX.marketdata.ws._stream'):
            systemEventWS()

    def test_tradingStatus(self):
        from pyEX import tradingStatusWS
        with patch('pyEX.marketdata.ws._stream'):
            tradingStatusWS()
            tradingStatusWS('test')

    def test_opHaltStatus(self):
        from pyEX import opHaltStatusWS
        with patch('pyEX.marketdata.ws._stream'):
            opHaltStatusWS()
            opHaltStatusWS('test')

    def test_ssrStatus(self):
        from pyEX import ssrStatusWS
        with patch('pyEX.marketdata.ws._stream'):
            ssrStatusWS()
            ssrStatusWS('test')

    def test_securityEvent(self):
        from pyEX import securityEventWS
        with patch('pyEX.marketdata.ws._stream'):
            securityEventWS()
            securityEventWS('test')

    def test_tradeBreak(self):
        from pyEX import tradeBreakWS
        with patch('pyEX.marketdata.ws._stream'):
            tradeBreakWS()
            tradeBreakWS('test')

    def test_auction(self):
        from pyEX import auctionWS
        with patch('pyEX.marketdata.ws._stream'):
            auctionWS()
            auctionWS('test')

# for Coverage
from mock import patch, MagicMock


class TestAll:
    def test_channels(self):
        from pyEX import DeepChannels
        DeepChannels.options()

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
        from pyEX import deepWS, PyEXception
        from pyEX.marketdata.ws import DeepChannels
        with patch('pyEX.marketdata.ws._stream'):
            deepWS()
            deepWS('test')
            deepWS('test', 'ssr')
            deepWS('test', DeepChannels.SSR)
            try:
                deepWS('test', 'test')
                assert False
            except PyEXception:
                pass
            try:
                deepWS('test', ['test'])
                assert False
            except PyEXception:
                pass
            try:
                deepWS('test', [DeepChannels.SSR, 'test'])
                assert False
            except PyEXception:
                pass

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

    def test_officialPrice(self):
        from pyEX import officialPriceWS
        with patch('pyEX.marketdata.ws._stream'):
            officialPriceWS()
            officialPriceWS('test')

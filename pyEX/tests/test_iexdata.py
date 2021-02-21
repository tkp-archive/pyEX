# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

# for Coverage
from mock import MagicMock, patch

SYMBOL = "aapl"


class TestAll:
    def test_tops(self):
        from pyEX import iexTops

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexTops()
            iexTops("test")
            iexTops(["test"])

    def test_topsDF(self):
        from pyEX import iexTopsDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexTopsDF()

    def test_last(self):
        from pyEX import iexLast

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexLast()
            iexLast("test")

    def test_lastDF(self):
        from pyEX import iexLastDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexLastDF()

    def test_hist(self):
        from datetime import datetime

        from pyEX import iexHist

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexHist()
            iexHist("201505")
            iexHist(datetime.today())

    def test_histDF(self):
        from pyEX import histDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexHistDF()

    def test_deep(self):
        from pyEX import iexDeep

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexDeep()
            iexDeep("test")

    def test_deepDF(self):
        from pyEX import iexDeepDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexDeepDF()
            iexDeepDF("test")

    def test_book(self):
        from pyEX import iexBook

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexBook()
            iexBook("test")

    def test_bookDF(self):
        from pyEX import iexBookDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexBookDF()
            iexBookDF("test")

    def test_trades(self):
        from pyEX import iexTrades

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexTrades()
            iexTrades("test")

    def test_tradesDF(self):
        from pyEX import iexTradesDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexTradesDF()
            iexTradesDF("test")

    def test_systemEvent(self):
        from pyEX import iexSystemEvent

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexSystemEvent()

    def test_systemEventDF(self):
        from pyEX import iexSystemEventDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexSystemEventDF()

    def test_tradingStatus(self):
        from pyEX import iexTradingStatus

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexTradingStatus()
            iexTradingStatus("test")

    def test_tradingStatusDF(self):
        from pyEX import iexTradingStatusDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexTradingStatusDF()
            iexTradingStatusDF("test")

    def test_opHaltStatus(self):
        from pyEX import iexOpHaltStatus

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexOpHaltStatus()
            iexOpHaltStatus("test")

    def test_opHaltStatusDF(self):
        from pyEX import iexOpHaltStatusDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexOpHaltStatusDF()
            iexOpHaltStatusDF("test")

    def test_ssrStatus(self):
        from pyEX import iexSsrStatus

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexSsrStatus()
            iexSsrStatus("test")

    def test_ssrStatusDF(self):
        from pyEX import iexSsrStatusDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexSsrStatusDF()
            iexSsrStatusDF("test")

    def test_securityEvent(self):
        from pyEX import iexSecurityEvent

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexSecurityEvent()
            iexSecurityEvent("test")

    def test_securityEventDF(self):
        from pyEX import iexSecurityEventDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexSecurityEventDF()
            iexSecurityEventDF("test")

    def test_tradeBreak(self):
        from pyEX import iexTradeBreak

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexTradeBreak()
            iexTradeBreak("test")

    def test_tradeBreakDF(self):
        from pyEX import iexTradeBreakDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexTradeBreakDF()
            iexTradeBreakDF("test")

    def test_auction(self):
        from pyEX import iexAuction

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexAuction()
            iexAuction("test")

    def test_auctionDF(self):
        from pyEX import iexAuctionDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexAuctionDF()
            iexAuctionDF("test")

    def test_officialPrice(self):
        from pyEX import iexOfficialPrice

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            iexOfficialPrice()
            iexOfficialPrice("test")

    def test_officialPriceDF(self):
        from pyEX import iexOfficialPriceDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            iexOfficialPriceDF()
            iexOfficialPriceDF("test")

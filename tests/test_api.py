# for Coverage
from mock import patch, MagicMock

C = 'AAPL'


class TestAPI:
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

    def test_symbols(self):
        from pyEX.refdata import symbols
        symbols()

    def test_corporateActions(self):
        from pyEX.refdata import corporateActions
        corporateActions()

    def test_dividends(self):
        from pyEX.refdata import dividends
        dividends()

    def test_nextDayExtDate(self):
        from pyEX.refdata import nextDayExtDate
        nextDayExtDate()

    def test_directory(self):
        from pyEX.refdata import directory
        directory()

    def test_company(self):
        from pyEX import company
        company(C)

    def test_quote(self):
        from pyEX import quote
        quote(C)

    def test_price(self):
        from pyEX import price
        price(C)

    def test_spread(self):
        from pyEX import spread
        spread(C)

    def test_volumeByVenue(self):
        from pyEX import volumeByVenue
        volumeByVenue(C)

    def test_delayedQuote(self):
        from pyEX import delayedQuote
        delayedQuote(C)

    def test_yesterday(self):
        from pyEX import yesterday
        yesterday(C)

    def test_marketYesterday(self):
        from pyEX import marketYesterday
        marketYesterday()

    def test_book(self):
        from pyEX import book
        book(C)

    def test_ohlc(self):
        from pyEX import ohlc
        ohlc(C)

    def test_marketOhlc(self):
        from pyEX import marketOhlc
        marketOhlc()

    def test_sstats(self):
        from pyEX import stockStats
        stockStats(C)

    def test_financials(self):
        from pyEX import financials
        financials(C)

    def test_earnings(self):
        from pyEX import earnings
        earnings(C)

    def test_peers(self):
        from pyEX import peers
        peers(C)

    def test_relevant(self):
        from pyEX import relevant
        relevant(C)

    def test_dividends2(self):
        from pyEX import dividends
        dividends(C)

    def test_splits(self):
        from pyEX import splits
        splits(C)

    def test_news(self):
        from pyEX import news
        news(C)

    def test_marketNews(self):
        from pyEX import marketNews
        marketNews()

    def test_chart(self):
        from pyEX import chart
        chart(C)

    def test_logo(symbol):
        from pyEX import logo
        logo(C)

    def test_list(self):
        from pyEX import list
        list()

    def test_companyDF(self):
        from pyEX import companyDF
        companyDF(C)

    def test_quoteDF(self):
        from pyEX import quoteDF
        quoteDF(C)

    def test_spreadDF(self):
        from pyEX import spreadDF
        spreadDF(C)

    def test_volumeByVenueDF(self):
        from pyEX import volumeByVenueDF
        volumeByVenueDF(C)

    def test_yesterdayDF(self):
        from pyEX import yesterdayDF
        yesterdayDF(C)

    def test_marketYesterdayDF(self):
        from pyEX import marketYesterdayDF
        marketYesterdayDF()

    def test_sstatsDF(self):
        from pyEX import stockStatsDF
        stockStatsDF(C)

    def test_dividendsDF(self):
        from pyEX import dividendsDF
        dividendsDF(C)

    def test_ohlcDF(self):
        from pyEX import ohlcDF
        ohlcDF(C)

    def test_marketOhlcDF(self):
        from pyEX import marketOhlcDF
        marketOhlcDF()

    def test_newsDF(self):
        from pyEX import newsDF
        newsDF(C)

    def test_marketNewsDF(self):
        from pyEX import marketNewsDF
        marketNewsDF()

    def test_listDF(self):
        from pyEX import listDF
        listDF()

    def test_logoPNG(self):
        from pyEX import logoPNG
        logoPNG(C)

    def test_logoNotebook(self):
        from pyEX import logoNotebook
        logoNotebook(C)

    def test_stats(self):
        from pyEX.stats import stats
        stats()

    def test_recent(self):
        from pyEX.stats import recent
        recent()

    def test_records(self):
        from pyEX.stats import records
        records()

    def test_summary(self):
        from datetime import datetime
        from pyEX.stats import summary
        summary()
        summary('201505')
        summary(datetime.today())

    def test_daily(self):
        from datetime import datetime
        from pyEX.stats import daily
        daily()
        daily('201505')
        daily(last='5')
        daily(datetime.today())

    def test_markets(self):
        from pyEX import markets
        markets()

    def test_tops(self):
        from pyEX import tops
        tops(C)
        tops([C])

    def test_last(self):
        from pyEX import last
        last(C)

    def test_hist(self):
        from datetime import datetime
        from pyEX import hist
        hist()
        hist('201505')
        hist(datetime.today())

    def test_deep(self):
        from pyEX import deep
        deep(C)

    def test_book2(self):
        from pyEX import topsBook
        topsBook(C)

    def test_trades(self):
        from pyEX import trades
        trades(C)

    def test_systemEvent():
        from pyEX import systemEvent
        systemEvent()

    def test_tradingStatus(self):
        from pyEX import tradingStatus
        tradingStatus(C)

    def test_opHaltStatus(self):
        from pyEX import opHaltStatus
        opHaltStatus(C)

    def test_ssrStatus(self):
        from pyEX import ssrStatus
        ssrStatus(C)

    def test_securityEvent(self):
        from pyEX import securityEvent
        securityEvent(C)

    def test_tradeBreak(self):
        from pyEX import tradeBreak
        tradeBreak(C)

    def test_auction(self):
        from pyEX import auction
        auction(C)

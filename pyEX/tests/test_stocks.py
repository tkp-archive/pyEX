# for Coverage
import time
from mock import patch, MagicMock
SYMBOL = 'aapl'


class TestAll:
    def teardown(self):
        time.sleep(.1)  # prevent being blocked

    def test_company(self):
        from pyEX import company
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            company('test')

    def test_companyDF(self):
        from pyEX import companyDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value={'test': [4], 'symbol': ['test']})
            companyDF('test')

    def test_quote(self):
        from pyEX import quote
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            quote('test')

    def test_quoteDF(self):
        from pyEX import quoteDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value={'test': [4], 'symbol': ['test']})
            quoteDF('test')

    def test_price(self):
        from pyEX import price
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            price('test')

    def test_priceDF(self):
        from pyEX import priceDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            priceDF('test')

    def test_priceTarget(self):
        from pyEX import priceTarget
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            priceTarget('test')

    def test_priceTargetDF(self):
        from pyEX import priceTargetDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            priceTargetDF('test')

    def test_spread(self):
        from pyEX import spread
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            spread(SYMBOL)

    def test_spreadDF(self):
        from pyEX import spreadDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            spreadDF(SYMBOL)

    def test_volumeByVenue(self):
        from pyEX import volumeByVenue
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            volumeByVenue('test')

    def test_volumeByVenueDF(self):
        from pyEX import volumeByVenueDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            volumeByVenueDF(SYMBOL)

    def test_delayedQuote(self):
        from pyEX import delayedQuote
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            delayedQuote('test')

    def test_delayedQuoteDF(self):
        from pyEX import delayedQuoteDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[{'symbol': 'test'}])
            delayedQuoteDF('test')

    def test_yesterday(self):
        from pyEX import yesterday
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            yesterday(SYMBOL)

    def test_yesterdayDF(self):
        from pyEX import yesterdayDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            yesterdayDF(SYMBOL)

    def test_marketYesterday(self):
        from pyEX import marketYesterday
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            marketYesterday()

    def test_marketYesterdayDF(self):
        from pyEX import marketYesterdayDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            marketYesterdayDF()

    def test_book(self):
        from pyEX import book
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            book('test')

    def test_bookDF(self):
        from pyEX import bookDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value={
                "quote": {'symbol': SYMBOL},
                "bids": [],
                "asks": [],
                "trades": [],
                "systemEvent": {},
            })

            bookDF(SYMBOL)

    def test_ohlc(self):
        from pyEX import ohlc
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            ohlc('test')

    def test_ohlcDF(self):
        from pyEX import ohlcDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            ohlcDF('test')

    def test_marketOhlc(self):
        from pyEX import marketOhlc
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            marketOhlc()

    def test_marketOhlcDF(self):
        from pyEX import marketOhlcDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            marketOhlcDF()

    def test_stats(self):
        from pyEX import keyStats
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            keyStats('test')

    def test_statsDF(self):
        from pyEX import keyStatsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[{'financials': [{'reportDate': 1}], 'symbol': 'aapl'}])
            keyStatsDF('test')

    def test_financials(self):
        from pyEX import financials
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            financials('test')

    def test_financialsDF(self):
        from pyEX import financialsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[{'financials': [{'reportDate': 1}], 'symbol': 'aapl'}])
            financialsDF('test')

    def test_fundOwnership(self):
        from pyEX import fundOwnership
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            fundOwnership('test')

    def test_fundOwnershipDF(self):
        from pyEX import fundOwnershipDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            fundOwnershipDF('test')

    def test_earnings(self):
        from pyEX import earnings
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            earnings('test')

    def test_earningsDF(self):
        from pyEX import earningsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            earningsDF(SYMBOL)

    def test_earningsToday(self):
        from pyEX import earningsToday
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            earningsToday()

    def test_earningsTodayDF(self):
        from pyEX import earningsTodayDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            earningsTodayDF()

    def test_peers(self):
        from pyEX import peers
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            peers('test')

    def test_peersDF(self):
        from pyEX import peersDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            peersDF('test')

    def test_sectorPerformance(self):
        from pyEX import sectorPerformance
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            sectorPerformance()

    def test_sectorPerformanceDF(self):
        from pyEX import sectorPerformanceDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            sectorPerformanceDF()

    def test_relevant(self):
        from pyEX import relevant
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            relevant('test')

    def test_relevantDF(self):
        from pyEX import relevantDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            relevantDF('test')

    def test_dividends(self):
        from pyEX import dividends
        from pyEX.common import PyEXception
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            dividends('test')

            try:
                dividends('test', 'test')
                assert False
            except PyEXception:
                pass

    def test_dividendsDF(self):
        from pyEX import dividendsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            dividendsDF(SYMBOL)

    def test_collections(self):
        from pyEX import collections
        from pyEX.common import PyEXception
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            collections('sector', 'test')

            try:
                collections('test', 'test')
                assert False
            except PyEXception:
                pass

    def test_collectionsDF(self):
        from pyEX import collectionsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            collectionsDF('sector', 'Health Care')

    def test_crypto(self):
        from pyEX import crypto
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            crypto()

    def test_cryptoDF(self):
        from pyEX import cryptoDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            cryptoDF()

    def test_stockSplits(self):
        from pyEX import stockSplits
        from pyEX.common import PyEXception
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            stockSplits(SYMBOL)
            try:
                stockSplits('test', 'test')
                assert False
            except PyEXception:
                pass

    def test_stockSplitsDF(self):
        from pyEX import stockSplitsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            stockSplitsDF(SYMBOL, '5y')

    def test_news(self):
        from pyEX import news
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            news('test')

    def test_newsDF(self):
        from pyEX import newsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            newsDF(SYMBOL)

    def test_marketNews(self):
        from pyEX import marketNews
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            marketNews()

    def test_marketNewsDF(self):
        from pyEX import marketNewsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            marketNewsDF()

    def test_chart(self):
        from pyEX import chart
        from pyEX.common import PyEXception
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            chart('test')
            try:
                chart('test', '5')
                assert False
            except PyEXception:
                pass
            chart('test', None)
            chart('test', None, '20150707')

    def test_chartDF(self):
        from pyEX import chartDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            chartDF(SYMBOL)

    def test_logo(symbol):
        from pyEX import logo
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            logo('test')

    def test_list(self):
        from pyEX import list
        from pyEX.common import PyEXception
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.json = MagicMock(return_value=[])
            mock.return_value.status_code = 200
            list()

            try:
                list('test')
                assert False
            except PyEXception:
                pass

    def test_listDF(self):
        from pyEX import listDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            listDF()

    def test_largestTrades(self):
        from pyEX import largestTrades
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.json = MagicMock(return_value=[])
            mock.return_value.status_code = 200
            largestTrades('aapl')

    def test_largestTradesDF(self):
        from pyEX import largestTradesDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            largestTradesDF(SYMBOL)

    def test_logoPNG(self):
        from pyEX import logoPNG
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.content = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x80\x00\x00\x00\x80\x08\x02\x00\x00\x00L\\\xf6\x9c\x00\x00\n\xb6IDATx\x9c\xec\x9d[L\x1bG\x17\xc7q\xec\x1a\x8c\xcd\xc5\x80/lJ\xb1[\x17\\q\x17\xb5LE)\x88r)\xa0\x8aV*\xa5j+\xd5P\xd16o\x89x\xe2%\x8a\x94\x87\x88\x87\xe4!R$\x1e\x10\xb9)Q\x94<D\x11\x84`D\x84b%$\x8a\xc1\xa0\x08\x19\x07\x0c\xe1"\x9c\x18\x10\x06c;\xc46\xebO\x1f\x96\xf8\xf8Bq<\xbb3\xde\x8b\xf9=&{\xce\x1c\xf6\xef\x99\xd9\x99=s\x96\x17\x08\x04b\x8e\xa0\x8ecT\x07\x10\xed\x1c\t@1<\xaa\x03\xa0\x92\xb5\xb55\xbb\xdd\xee\xf1x\xf2\xf2\xf2\xe2\xe2\xe2(\x89!\xba\x04\xf0z\xbdf\xb3y~~\xdej\xb5.--moo\x07\xff\xfd\xec\xd9\xb3G\x02\xa0\xc5\xeb\xf5>}\xfa\xb4\xb7\xb7wkk\x8b\xeaX\xfe\x0f\xf6\x0b\xe0\xf3\xf9\x06\x07\x07\x1f>|\xe8v\xbb\x0f\xbb\x86\xcb\xe5F6\xa8\xff\xc1r\x01,\x16\xcb\x95+W\x1c\x0eG\xe8\xcb\xa8\x1a\x7fX.\xc0\xf8\xf8xWWW8W\xf2\xf9|\xf4\xe1\xfc;\xec\x14\xc0\xef\xf7\x0f\x0e\x0e\xde\xbf\x7f?\x9c\x8b\xc5b\xf1G\x1f}\x84>\xa8\x7f\x87\x85\x02\xf8\xfd\xfe\x8b\x17/\xbe|\xf92\xcc\xeb?\xfb\xec3\xc4\x11\x85\x82\x85\x0b\xb1\xfe\xfe\xfe\xf0\xef~LLLFF\x06\xcap>\x00\xdb\x040\x18\x0cz\xbd\x1e\xc8\xa4\xb0\xb0\x10Y8\x1f\x86UC\xd0\x8b\x17/n\xdc\xb8\x01d\xa2R\xa9\xe4r9\xb2\x88>\x0c{z\x00\x8e\xe3\xbd\xbd\xbd\xa0V\x1a\x8d\x06M8\xe1\xc2\x12\x01\x02\x81\xc0\xf5\xeb\xd7\x17\x17\x17\x81\xacD"\xd1W_}\x85,\xa8\xb0`\x89\x00z\xbd~dd\x04\xd4J\xa3\xd1\xc4\xc6\xc6\xa2\x89(\\\xd8 \x80\xcb\xe5\n\xf3\x91\xff=\x8a\x8a\x8a\x10\x84\x03\x06\x1b\x04\x18\x1a\x1a\xf2z\xbd\xa0V\xf9\xf9\xf9YYYh"\x02\x80\xf1\x02\xe08n0\x18@\xad\x84B\xe1\x9f\x7f\xfe\xc9\xe1p\xd0\x04\x05\x00\xe3\x050\x18\x0c!\xb69\x0f\xa3\xb1\xb1\x91\xc2\r\xb8\xfd0[\x00\x1c\xc7\x07\x06\x06@\xad\n\n\n\xca\xcb\xcb\xd1D\x04\x0c\xb3\x05XZZ\xfa\xe0V\xf3{H\xa5R\x9dN\x87,"`\x98\xbd\x126\x1a\x8d@\xd7\xcb\xe5\xf2\xf6\xf6\xf6\xf8\xf8xd\x11\x01\xc3\xec\x1e`\xb1X\xc2\xbf\x98\xcb\xe5\xfe\xf3\xcf?\x89\x89\x89(#\x02\x86\xc1=\x00\xc7\xf1\xa5\xa5\xa50/\x16\x08\x04mmm\xe9\xe9\xe9\x88\x83\x02\x86\xc1\x028\x9d\xce0\xafT*\x95\xad\xad\xadR\xa9\x14qDD`\xb0\x00a.\xbe\x8a\x8a\x8aZ[[)|\xe9\x18\x1a\x06\x0b\xb0\xb3\xb3\x13\xfa\x82\xf8\xf8\xf8_\x7f\xfd\x95\xf2\xfd\xce\xd00X\x80\x10\xb9$\x99\x99\x99\x85\x85\x85\xa5\xa5\xa5III\x91\r\n\x18\x06\x0bp\xf0M\xbaD"\xc9\xcd\xcd-//\xa7\xe1d{\x18\x1cF\xa7\xa7\xbb\\.\x8f\xc7\xf3\xdf?\x83\xc3IHH\xa0\xc9\xee\x02\x10\x14\x08\xb0\xb3\xb3\xb3\xb9\xb9\xb9\xb6\xb6\xb6\xb1\xb1\xb1\xbd\xbd\x1d\x08\x04\xde\xbd{\'\x10\x08\x12\x13\x13SRRd2\x19\xa2\tsggguu\xd5f\xb3mlllnn:\x1c\x0e\xbf\xdf\x1f\xfc/\x0e\x87\x93\x98\x98(\x14\n\x93\x92\x92\xa4R\xa9L&KJJ\x8a\xccV]\xe4\x86 \xa7\xd3i6\x9b\x8dF\xe3\xd4\xd4T\x88\xf9\x93\xc7\xe3egg\xabT*\xadV\x9b\x9a\x9a\n\xa5]\x93\xc94111;;\x1b\xfe\xaeujj\xaaF\xa3\xf9\xfa\xeb\xaf%\x12\t\xf9\x18B\x80\xbc\x07\xb8\xdd\xee\xd1\xd1Q\x93\xc9\x04\xb4j\rr|\x97\xdc\xdc\xdc\x9c\x9c\x1c\x91H\x14\xbe\xa1\xc3\xe1\x98\x9b\x9b3\x9b\xcd\xd3\xd3\xd3+++\xa0\xed\xee\xc1\xe1p\xe4r\xb9F\xa3\xd1j\xb5iii\x84\xfd\x84j\x02\x9d\x00\xc1\xb7\xe4\x8f\x1e="\xb0]|\x10\xa5RY^^\xae\xd1hx\xbcC{m \x10\xb0X,z\xbd~jj\x8a|\x8b\xfb\xe1\xf1x\xf5\xf5\xf5\xd5\xd5\xd5\xd0\x87GT\x02\xac\xad\xaduuu\x85\xbfU\x10&\x02\x81\xa0l\x97\xf7\x96\xb58\x8eONN>x\xf0`nn\x0en\x8b\xfbIKK;q\xe2\xc4\xc7\x1f\x7f\x0c\xd1\'|\x01\xfc~\xff\xe3\xc7\x8f{{{].\x17\\\xcf\xfb\x11\x8b\xc5*\x95J\xa9T\xfa|>\xab\xd5:33\xb3w\xda\x02)\x02\x81\xa0\xae\xae\xae\xb2\xb2\x12V:)d\x01\\.\xd7\xf9\xf3\xe7m6\x1bD\x9f4\x04\xc3\xb0S\xa7NA\xd9X\x85\xb9\x1d\x8d\xe3xOO\x0f\xeb\xef~LL\x8c\xcdf\x03M\xc1;\x0ch=`ee\xe5\xea\xd5\xabV\xab\x15\x8a7FPXX\xf8\xdbo\xbf\x91\xec\x07p\x04p:\x9d\xa7O\x9f~\xfb\xf6-yW\xccB.\x97wtt\x90Y\x81\xc3\x19\x82\xee\xdc\xb9\x13\x85w?&&\xe6\xcd\x9b7CCCd<@\x10\xa0\xaf\xaf\xef\xf9\xf3\xe7\xe4\xfd0\x14\xbd^?33C\xd8\x9c\xac\x00\xc3\xc3\xc3\x04r\x92\xd9\x84H$:v\x8c\xf8m$\xb5\x17\xf4\xea\xd5\xab\xdb\xb7o\x93\xf1\xc0h\xf8|~iii}}=\x99y\x98\x94\x00w\xef\xde\xc5q\x9c\x8c\x07\xe6\x92\x92\x92r\xf2\xe4I\x99LF\xd2\x0f\xf1\xbe3??\x0ft\x14\x8bMp\xb9\xdc\xbf\xfe\xfa\x8b\xfc\xdd\'\xde\x03|>_OO\x0f\xf9\xe6\x99\x88J\xa5\xfa\xe3\x8f?`\xe5X\x10\x14\xc0d2\xd9\xedv(\x110\x0b\x0c\xc3\xda\xdb\xdb\xc9\xcc\xba\xefA\xd0\xd1\xf8\xf88\xac\x08\x98Ess3\xc4\xbbOP\x00\x87\xc3199\t1\x08\xa6\xf0\xd3O?\xa9\xd5j\xb8>\x89\x08044\xe4\xf3\xf9\xe0\xc6A\x7f***\xaa\xab\xab\xa1\xbb\x05\x16\x00\xc7q\xd0\x9cd\x16\x10\x17\x17\xf7\xe3\x8f?\xa2\xf0\x0c,\x80\xc9d\xda\xdc\xdcD\x11\n\x9d\xa9\xa8\xa8@\x94\xf3\x02,\x00\x81\xd3\xa0,\x00\xdd\x89\x1a0\x01\xfc~?\x81\xe4\x06\xa6\x93\x95\x95\x95\x92\x92\x82\xc89\x98\x00\xcb\xcb\xcb\x1fL\x89e\x1f(\xe6\xde=\xc0\x04\x80\x9e\xe5@\x7fD"Q~~>:\xff`\x02\xbc~\xfd\x1aY$4\x05u9\'0\x01\xc8d\x991\x14\xb8Y@\x07\x01\x13\x00J\x8e\x1b\xb3@\x94\x91\xb8\x07\x98\x00\xd1\xb6\x02\x10\n\x85\xe8\x9e\x7f\x82\x80\t\xb0\xbe\xbe\x8e,\x12:\x92\xb2\x0b\xd2&\x00\x04\xf0\xfb\xfd\xd1\xf6\xfe+~\x17\xa4M\x00\x08\x804\xd7\x93\x9epvA\xda\x04\xb3O\xca\xa3\xe6\xd8.h\x9b@\xea\x9d\xe9\xe0\xbb m\x02@\x80(\xdc\x84\x88\x00\x00\x02PX\xe3\x9d*\xde\xee\x82\xb4\x89\xa3!(\x14\x8e]\x906\x01 \x00m\xcb-\xa0\xc3\xe9t\xae\xae\xae"m\x02@\x00Z\xd59\x8a\x18\xa8\xd7\x9e`C\x90P(D\x16\tMYXX@\xea\x1fL\x00\xfa\xd7\xbe\x80\x8e\xd5jE\xfa$\n&@\x14\x8eB\x1e\x8f\x07\xe9\xd1W0\x01\xe8Vp-2\xf4\xf5\xf5\xa1s\x0e&\x00=\xab~\xa1fjj\n\xdd\xd1\xcf\xa3\x1e\x10\x16\x13\x13\x13\x88<\x83\t\x80\xbat\x08m1\x18\x0c\x88N\xe2\x83\t\x80a\x18\x8a \xe8\x8f\xc3\xe1@t\x18\x0bL\x80\xe4\xe4\xe4(\xdc\x11\n\xf2\xe4\xc9\x13\xb3\xd9\x0c\xdd-\x98\x00<\x1e\x8f\x0e5\xf7\xa9\xa2\xbb\xbb\x1b\xfa\xb1\x14\xe0\xcd\xb8\x9c\x9c\x1c\xb8\x110\x08\xb7\xdb}\xf3\xe6M\xb8>\x81\x05\xa0\xf6\xab[\x94c\xb1X\xba\xbb\xbb!N\xc8\xc0\x02H$\x92\xcc\xccLX\xcd3\x11\xa3\xd1\xd8\xd9\xd9\tK\x03"\xef\x03\xbe\xf8\xe2\x0b(m3\x17\x9b\xcdv\xed\xda5(\xae\x88\x08@\xf9\xb7\xb7\xe8\xc0\xd8\xd8Xgg\'\xf9\x93\xd2D\x04\x90\xefB\xb2a\x16077w\xe1\xc2\x85{\xf7\xee\x91qB\xf0\x95d\x94O\x03\xfb\xe9\xef\xef\xbft\xe9R\xf8\xb5\xf4\xdf\x83{\xe6\xcc\x19\x02f>\x9f/j\x8f\n\x1f\xc4n\xb7\x8f\x8c\x8cx<\x9e\xb8\xb88\xb1X\x0cdK\xf0\xa4|^^\x1e1C\xb6\xe2v\xbb\x07\x06\x06\xb6\xb6\xb6\x94J%\x90!\xc1!H \x10D\xf3\x8a\xec0\x8a\x8b\x8bAM\x88\xa7\xa5\xd4\xd6\xd6\x12\xb6e%2\x99\x8c\xc09z\xe2\x02dgg3\xa8L\x7f\x04\xa8\xae\xae&\xb0SI*1\xeb\xcb/\xbf$c\xce&\x12\x12\x12JJJ\x08\x18\x92\x12 77\x97\x8c9\x9b\xc8\xca\xca"V\xcc\x98\x94\x00\n\x85"\x9aw\xa7\xf7C\xf8SAdsC\x7f\xfe\xf9\xe7\x10\xf5\xe4\xa3\x84\xe0\xb7k\x88\xd9\x92\x15 ##\xe3\xdbo\xbf%\xe9\x84\xe9466\x12.\xa6\x0e!;\xba\xa6\xa6&\x9a;\x81X,&\xf0\xf8\xbf\x07\x04\x01D"\x11\xb1\x07\x00vPVVF\xe6\x18\x13\x9c\xf3\x01555P\xfc0\x0e>\x9f_QQA\xc6\x03\x1c\x01d2\x99V\xab\x85\xe2\x8aY\xd4\xd4\xd4\x90\xcc\x18\x87vB\xa6\xb9\xb99\xda^\x12\xa8T\xaa\xef\xbe\xfb\x8e\xa4\x13h\x02\x08\x85\xc2\xbf\xff\xfe\x1b\xf5\xa1N\xfa\xc0\xe7\xf3\xdb\xda\xda\xc8\x7fI\x06\xe6\xfd\xc20\xac\xa0\xa0\x00\xa2C:\xa3\xd1h\x92\x93\x93\xc9\xfb\x81\xfc\x83\xfd\xe1\x87\x1f\x98\xf8AGP\xe2\xe3\xe3\xeb\xea\xea\xa0\xb8\x82,\x80\\.\xd7\xe9tp}\xd2\x10\x9dN\x07+O\x19\xfe\x90]TT\xd4\xd4\xd4\x04\xdd-}hjj\x828\xd2"\x993\xab\xaa\xaa\xd8\x9a@\x97\x9f\x9f_UU\x05\xd1!\xaa\x87\x96\x86\x86\x06D\x9e\xa9\x05\xfa\xdf\x85J\x80O>\xf9\xa4\xa5\xa5\x85M\xb9\xec<\x1eO\xa7\xd3)\x14\n\xb8n\x11>\xb6\x97\x94\x94\x90\\\xa6\xd3\n\x9dN\x87"%\x10\xed\xba\xa9\xa1\xa1\x81\xccN!}(..&\xfc\xca%4h\x05\x10\n\x85\xcd\xcd\xcdLO\xa3S\xa9T\xbf\xfc\xf2\x0b"\xe7\x91\xf8\xa6\xbc\xd7\xeb=w\xee\x1cC?\xf2\x89aXGG\x07\xbaB%\x91\xd8\xba\xe1\xf3\xf9:\x9d\x8e\x89\x132\x86a:\x9d\x0ei\x99\x98H\xf4\x80 \x0b\x0b\x0b\xb7n\xdd"\x7f\xec_\xa1P|\xfa\xe9\xa7R\xa9\xf4\xf8\xf1\xe3iii\xb1\xb1\xb1\xc1\x8f\x99omm\xd9\xed\xf6\x95\x95\x95\x85\x85\x85\xc5\xc5E\xf2E~\xd5juKK\x0b\x94\r\x9f\x10DN\x80 \x97/_~\xf6\xec\x19\x01C\x0c\xc3\xbe\xf9\xe6\x1b\xadV\x1bf\xbd\n\x8f\xc73::j4\x1a\xa7\xa7\xa7\t4WVV\xf6\xfb\xef\xbf\x130\x04%\xd2\x02\x04\xbf\xf4\xaf\xd7\xeb\xc3\xac@\'\x10\x084\x1aMee%\xe1,<\xa7\xd3i\xd8%\xcc\xb2\xbf\\.\xb7\xb6\xb6\xf6\xfb\xef\xbf\x8f\xcc\xd6z\xa4\x05\x08\xe2t:\x87\x87\x87GGG\x0f\x0e\x14\x1c\x0e\x07\xc3\xb0\xf4\xf4\xf4\xcf?\xff\\\xadVK$\x12(\x93G \x10\xb0\xdb\xedf\xb3yvv\xd6n\xb7\xdbl\xb6\x83\xbf\x80\x84\x84\x04\xadV[UU\x05\x9abN\x06j\x04\xd8c}}}lllqq\xd1\xedv\'\'\'+\x14\x8a\x82\x82\x82\x08T%\xf2z\xbd\xf3\xf3\xf3\xcb\xcb\xcb\xc1r\xe4\xb1\xb1\xb1j\xb5:##\x03u\xbb\x07\xa1X\x80#\xa2\xe5\r"m9\x12\x80b\x8e\x04\xa0\x98#\x01(\xe6?\x01\x00\x00\xff\xff\xa9\xa6\x8d\xe1m\x0f@\x02\x00\x00\x00\x00IEND\xaeB`\x82'
            logoPNG('test')

    # def test_logoNotebook(self):
    #     from pyEX import logoNotebook
    #     with patch('requests.get') as mock, \
    #          patch('pickle.dump'), \
    #          patch('os.fspath'):
    #         mock.return_value = MagicMock()
    #         mock.return_value.status_code = 200
    #         mock.return_value.json.return_value = {'url': 'test'}
    #         logoNotebook('test')

    def test_threshold(self):
        from pyEX import threshold
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            threshold()
            threshold('20170707')

    def test_thresholdDF(self):
        from pyEX import thresholdDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            thresholdDF('test')

    def test_shortInterest(self):
        from pyEX import shortInterest
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            shortInterest('test')
            shortInterest('test', '20170707')

    def test_shortInterestDF(self):
        from pyEX import shortInterestDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            shortInterestDF('test')

    def test_marketShortInterest(self):
        from pyEX import marketShortInterest
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            marketShortInterest()
            marketShortInterest('20170707')

    def test_marketShortInterestDF(self):
        from pyEX import marketShortInterestDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            marketShortInterestDF()

    def test_ipo(self):
        from pyEX import ipoToday, ipoUpcoming
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            ipoToday()
            ipoUpcoming()

    def test_ipoDF(self):
        from pyEX import ipoTodayDF, ipoUpcomingDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value={'rawData': [{'symbol': 'test'}]})
            ipoTodayDF()
            ipoUpcomingDF()

    def test_balancesheet(self):
        from pyEX import balanceSheet
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            balanceSheet(SYMBOL)

    def test_balancesheetDF(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.balanceSheetDF(SYMBOL)

    def test_cashflow(self):
        from pyEX import cashFlow
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            cashFlow(SYMBOL)

    def test_cashflowDF(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.cashFlowDF(SYMBOL)

    def test_income(self):
        from pyEX import incomeStatement
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            incomeStatement(SYMBOL)

    def test_incomeDF(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.incomeStatementDF(SYMBOL)

    def test_estimates(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.estimates(SYMBOL)
            c.estimatesDF(SYMBOL)

    def test_marketVolume(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.marketVolume()
            c.marketVolumeDF()

    def test_insiderRoster(self):
        from pyEX import insiderRoster
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            insiderRoster(SYMBOL)

    def test_insiderRosterDF(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.insiderRosterDF(SYMBOL)

    def test_insiderSummary(self):
        from pyEX import insiderSummary
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            insiderSummary(SYMBOL)

    def test_insiderSummaryDF(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.insiderSummaryDF(SYMBOL)

    def test_insiderTransactions(self):
        from pyEX import insiderTransactions
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            insiderTransactions(SYMBOL)

    def test_insiderTransactionsDF(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.insiderTransactionsDF(SYMBOL)

    def test_institutionalOwnership(self):
        from pyEX import institutionalOwnership
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            institutionalOwnership(SYMBOL)

    def test_institutionalOwnershipDF(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.institutionalOwnershipDF(SYMBOL)

    def test_intraday(self):
        from pyEX import intraday
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            intraday(SYMBOL)

    def test_intradayDF(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.intradayDF(SYMBOL)

    def test_optionExpirations(self):
        from pyEX import optionExpirations
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            optionExpirations(SYMBOL)

    def test_options(self):
        from pyEX import options
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            options(SYMBOL, 'test')

    def test_optionsDF(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])

            c = Client(version='sandbox')
            c.optionsDF(SYMBOL, 'test')

    def test_bonusIssue(self):
        from pyEX import bonusIssue
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            bonusIssue()
            bonusIssue(SYMBOL)
            bonusIssue(SYMBOL, 'test')

    def test_bonusIssueDF(self):
        from pyEX import bonusIssueDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            bonusIssueDF()
            bonusIssueDF(SYMBOL)
            bonusIssueDF(SYMBOL, 'test')

    def test_distribution(self):
        from pyEX import distribution
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            distribution()
            distribution(SYMBOL)
            distribution(SYMBOL, 'test')

    def test_distributionDF(self):
        from pyEX import distributionDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            distributionDF()
            distributionDF(SYMBOL)
            distributionDF(SYMBOL, 'test')

    def test_returnOfCapital(self):
        from pyEX import returnOfCapital
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            returnOfCapital()
            returnOfCapital(SYMBOL)
            returnOfCapital(SYMBOL, 'test')

    def test_returnOfCapitalDF(self):
        from pyEX import returnOfCapitalDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            returnOfCapitalDF()
            returnOfCapitalDF(SYMBOL)
            returnOfCapitalDF(SYMBOL, 'test')

    def test_rightsIssue(self):
        from pyEX import rightsIssue
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            rightsIssue()
            rightsIssue(SYMBOL)
            rightsIssue(SYMBOL, 'test')

    def test_rightsIssueDF(self):
        from pyEX import rightsIssueDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            rightsIssueDF()
            rightsIssueDF(SYMBOL)
            rightsIssueDF(SYMBOL, 'test')

    def test_rightToPurchase(self):
        from pyEX import rightToPurchase
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            rightToPurchase()
            rightToPurchase(SYMBOL)
            rightToPurchase(SYMBOL, 'test')

    def test_rightToPurchaseDF(self):
        from pyEX import rightToPurchaseDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            rightToPurchaseDF()
            rightToPurchaseDF(SYMBOL)
            rightToPurchaseDF(SYMBOL, 'test')

    def test_securityReclassification(self):
        from pyEX import securityReclassification
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            securityReclassification()
            securityReclassification(SYMBOL)
            securityReclassification(SYMBOL, 'test')

    def test_securityReclassificationDF(self):
        from pyEX import securityReclassificationDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            securityReclassificationDF()
            securityReclassificationDF(SYMBOL)
            securityReclassificationDF(SYMBOL, 'test')

    def test_securitySwap(self):
        from pyEX import securitySwap
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            securitySwap()
            securitySwap(SYMBOL)
            securitySwap(SYMBOL, 'test')

    def test_securitySwapDF(self):
        from pyEX import securitySwapDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            securitySwapDF()
            securitySwapDF(SYMBOL)
            securitySwapDF(SYMBOL, 'test')

    def test_spinoff(self):
        from pyEX import spinoff
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            spinoff()
            spinoff(SYMBOL)
            spinoff(SYMBOL, 'test')

    def test_spinoffDF(self):
        from pyEX import spinoffDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            spinoffDF()
            spinoffDF(SYMBOL)
            spinoffDF(SYMBOL, 'test')

    def test_splits(self):
        from pyEX import splits
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            splits()
            splits(SYMBOL)
            splits(SYMBOL, 'test')

    def test_splitsDF(self):
        from pyEX import splitsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            splitsDF()
            splitsDF(SYMBOL)
            splitsDF(SYMBOL, 'test')

    def test_upcomingEvents(self):
        from pyEX import upcomingEvents, upcomingEarnings, upcomingDividends, upcomingSplits, upcomingIPOs
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            upcomingEvents()
            upcomingEarnings()
            upcomingDividends()
            upcomingSplits()
            upcomingIPOs()
            upcomingEvents(SYMBOL)
            upcomingEarnings(SYMBOL)
            upcomingDividends(SYMBOL)
            upcomingSplits(SYMBOL)
            upcomingIPOs(SYMBOL)

    def test_upcomingEventsDF(self):
        from pyEX import upcomingEventsDF, upcomingEarningsDF, upcomingDividendsDF, upcomingSplitsDF, upcomingIPOsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            upcomingEventsDF()
            upcomingEarningsDF()
            upcomingDividendsDF()
            upcomingSplitsDF()
            upcomingIPOsDF()
            upcomingEventsDF(SYMBOL)
            upcomingEarningsDF(SYMBOL)
            upcomingDividendsDF(SYMBOL)
            upcomingSplitsDF(SYMBOL)
            upcomingIPOsDF(SYMBOL)

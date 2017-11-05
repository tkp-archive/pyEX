# for Coverage
from pyEX import api
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

    def test_company(self):
        from pyEX import company
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            company('test')

    def test_quote(self):
        from pyEX import quote
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            quote('test')

    def test_price(self):
        from pyEX import price
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            price('test')

    def test_spread(self):
        from pyEX import spread
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            spread('test')

    def test_volumeByVenue(self):
        from pyEX import volumeByVenue
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            volumeByVenue('test')

    def test_delayedQuote(self):
        from pyEX import delayedQuote
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            delayedQuote('test')

    def test_yesterday(self):
        from pyEX import yesterday
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            yesterday('test')

    def test_marketYesterday(self):
        from pyEX import marketYesterday
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            marketYesterday()

    def test_book(self):
        from pyEX import book
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            book('test')

    def test_openClose(self):
        from pyEX import openClose
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            openClose('test')

    def test_marketOpenClose(self):
        from pyEX import marketOpenClose
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            marketOpenClose()

    def test_stats(self):
        from pyEX import stats
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            stats('test')

    def test_financials(self):
        from pyEX import financials
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            financials('test')

    def test_earnings(self):
        from pyEX import earnings
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            earnings('test')

    def test_peers(self):
        from pyEX import peers
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            peers('test')

    def test_relevant(self):
        from pyEX import relevant
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            relevant('test')

    def test_dividends(self):
        from pyEX import dividends
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            dividends('test')

    def test_splits(self):
        from pyEX import splits
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            splits('test')

    def test_news(self):
        from pyEX import news
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            news('test')

    def test_marketNews(self):
        from pyEX import marketNews
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            marketNews()

    def test_chart(self):
        from pyEX import chart
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            chart('test')

    def test_logo(symbol):
        from pyEX import logo
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            logo('test')

    def test_list(self):
        from pyEX import list
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            list()

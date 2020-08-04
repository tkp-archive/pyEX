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

    def test_symbols(self):
        from pyEX.refdata import symbols, iexSymbols, mutualFundSymbols, otcSymbols, internationalSymbols, fxSymbols
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            symbols()
            iexSymbols()
            mutualFundSymbols()
            otcSymbols()
            internationalSymbols()
            internationalSymbols('GB')
            internationalSymbols(exchange='test')
            mock.return_value.json = MagicMock(return_value={'currencies': [], 'pairs': []})
            fxSymbols()

    def test_symbolsDF(self):
        from pyEX.refdata import symbolsDF
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            c = Client(version='sandbox')
            symbolsDF()
            c.iexSymbolsDF()
            c.mutualFundSymbolsDF()
            c.otcSymbolsDF()
            c.internationalSymbolsDF()
            c.internationalSymbolsDF('GB')
            c.internationalSymbolsDF(exchange='test')

            c.symbolsList()
            c.iexSymbolsList()
            c.mutualFundSymbolsList()
            c.otcSymbolsList()
            c.internationalSymbolsList()
            c.internationalSymbolsList('GB')
            c.internationalSymbolsList(exchange='test')

            mock.return_value.json = MagicMock(return_value={'currencies': [], 'pairs': []})
            c.fxSymbolsDF()
            c.fxSymbolsList()

    def test_calendar(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            c = Client(version='sandbox')
            c.calendar()
            c.holidays()

    def test_calendarDF(self):
        from pyEX import Client
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            c = Client(version='sandbox')
            c.calendarDF()
            c.holidaysDF()

    def test_corporateActions(self):
        from pyEX.refdata import corporateActions
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            corporateActions()
            corporateActions('20170202')

    def test_corporateActionsDF(self):
        from pyEX.refdata import corporateActionsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            corporateActionsDF()

    def test_dividends(self):
        from pyEX.refdata import refDividends
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            refDividends()
            refDividends('20170202')

    def test_dividendsDF(self):
        from pyEX.refdata import refDividendsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            refDividendsDF()

    def test_nextDayExtDate(self):
        from pyEX.refdata import nextDayExtDate
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            nextDayExtDate()
            nextDayExtDate('20170202')

    def test_nextDayExtDateDF(self):
        from pyEX.refdata import nextDayExtDateDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            nextDayExtDateDF()

    def test_directory(self):
        from pyEX.refdata import directory
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            directory()
            directory('20170202')

    def test_directoryDF(self):
        from pyEX.refdata import directoryDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            directoryDF()

    def test_sectors(self):
        from pyEX.refdata import sectors
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            sectors()

    def test_sectorsDF(self):
        from pyEX.refdata import sectorsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            sectorsDF()

    def test_exchanges(self):
        from pyEX.refdata import exchanges, internationalExchanges
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            exchanges()
            internationalExchanges()

    def test_exchangesDF(self):
        from pyEX.refdata import exchangesDF, internationalExchangesDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            exchangesDF()
            internationalExchangesDF()

    def test_tags(self):
        from pyEX.refdata import tags
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            tags()

    def test_tagsDF(self):
        from pyEX.refdata import tagsDF
        with patch('requests.get') as mock, \
                patch('pickle.dump'):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            tagsDF()

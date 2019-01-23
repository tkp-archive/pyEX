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
        from pyEX.refdata import symbols
        from pyEX.refdata import iexSymbols
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            symbols()
            iexSymbols()

    def test_symbolsDF(self):
        from pyEX.refdata import symbolsDF, iexSymbolsDF
        symbolsDF()
        iexSymbolsDF()

    def test_corporateActions(self):
        from pyEX.refdata import corporateActions
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            corporateActions()
            corporateActions('20170202')

    def test_corporateActionsDF(self):
        from pyEX.refdata import corporateActionsDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            corporateActionsDF()

    def test_dividends(self):
        from pyEX.refdata import dividends
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            dividends()
            dividends('20170202')

    def test_dividendsDF(self):
        from pyEX.refdata import dividendsDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            dividendsDF()

    def test_nextDayExtDate(self):
        from pyEX.refdata import nextDayExtDate
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            nextDayExtDate()
            nextDayExtDate('20170202')

    def test_nextDayExtDateDF(self):
        from pyEX.refdata import nextDayExtDateDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            nextDayExtDateDF()

    def test_directory(self):
        from pyEX.refdata import directory
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            directory()
            directory('20170202')

    def test_directoryDF(self):
        from pyEX.refdata import directoryDF
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            directoryDF()

# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

import atexit
import pickle

# for Coverage
from mock import MagicMock, patch

atexit.register = MagicMock()
pickle.dump = MagicMock()


class TestAll:
    def test_symbols(self):
        from pyEX import Client

        c = Client()
        c.symbols()
        c.iexSymbols()
        c.mutualFundSymbols()
        c.otcSymbols()
        c.internationalSymbols()
        c.internationalSymbols("GB")
        c.internationalSymbols(exchange="test")
        c.optionsSymbols()
        c.optionsSymbols("SPY")
        # c.optionsSymbols("SPY", "20291230")  # TODO reenable, sandbox on older version
        c.futuresSymbols()
        c.futuresSymbols("NG")
        c.fxSymbols()

        c.symbolsDF()
        c.iexSymbolsDF()
        c.mutualFundSymbolsDF()
        c.otcSymbolsDF()
        c.internationalSymbolsDF()
        c.internationalSymbolsDF("GB")
        c.internationalSymbolsDF(exchange="test")
        c.optionsSymbolsDF()
        c.optionsSymbolsDF("SPY")
        # c.optionsSymbolsDF("SPY", "20291230")  # TODO reenable, sandbox on older version
        c.futuresSymbolsDF()
        c.futuresSymbolsDF("NG")
        c.fxSymbolsDF()

        c.symbolsList()
        c.iexSymbolsList()
        c.mutualFundSymbolsList()
        c.otcSymbolsList()
        c.internationalSymbolsList()
        c.internationalSymbolsList("GB")
        c.internationalSymbolsList(exchange="test")
        c.optionsSymbolsList()
        c.optionsSymbolsList("SPY")
        # c.optionsSymbolsList("SPY", "20291230")  # TODO reenable, sandbox on older version
        c.futuresSymbolsList()
        c.futuresSymbolsList("NG")
        c.fxSymbolsList()

    def test_calendar(self):
        from pyEX import Client

        c = Client(version="sandbox")
        c.calendar()
        c.holidays()

    def test_calendarDF(self):
        from pyEX import Client

        c = Client(version="sandbox")
        c.calendarDF()
        c.holidaysDF()

    def test_corporateActions(self):
        from pyEX.refdata import corporateActions

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            corporateActions()
            corporateActions("20170202")

    def test_corporateActionsDF(self):
        from pyEX.refdata import corporateActionsDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            corporateActionsDF()

    def test_dividends(self):
        from pyEX.refdata import refDividends

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            refDividends()
            refDividends("20170202")

    def test_dividendsDF(self):
        from pyEX.refdata import refDividendsDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            refDividendsDF()

    def test_nextDayExtDate(self):
        from pyEX.refdata import nextDayExtDate

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            nextDayExtDate()
            nextDayExtDate("20170202")

    def test_nextDayExtDateDF(self):
        from pyEX.refdata import nextDayExtDateDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            nextDayExtDateDF()

    def test_directory(self):
        from pyEX.refdata import directory

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            directory()
            directory("20170202")

    def test_directoryDF(self):
        from pyEX.refdata import directoryDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            directoryDF()

    def test_sectors(self):
        from pyEX.refdata import sectors

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            sectors()

    def test_sectorsDF(self):
        from pyEX.refdata import sectorsDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            sectorsDF()

    def test_exchanges(self):
        from pyEX.refdata import exchanges, internationalExchanges

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            exchanges()
            internationalExchanges()

    def test_exchangesDF(self):
        from pyEX.refdata import exchangesDF, internationalExchangesDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            exchangesDF()
            internationalExchangesDF()

    def test_figi(self):
        from pyEX.refdata import figi

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            figi("")

    def test_figiDF(self):
        from pyEX.refdata import figiDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            figiDF("")

    def test_tags(self):
        from pyEX.refdata import tags

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            tags()

    def test_tagsDF(self):
        from pyEX.refdata import tagsDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            tagsDF()

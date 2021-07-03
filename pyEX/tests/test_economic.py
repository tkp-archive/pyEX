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


class TestEconomic:
    def test_all(self):
        from pyEX import Client

        c = Client("test")
        with patch("pyEX.common.urls._getIEXCloud"):
            c.us30()
            c.us30History()
            c.us30HistoryDF()
            c.us15()
            c.us15History()
            c.us15HistoryDF()
            c.us5()
            c.us5History()
            c.us5HistoryDF()
            c.fedfunds()
            c.fedfundsHistory()
            c.fedfundsHistoryDF()
            c.creditcard()
            c.cdnj()
            c.cdj()
            c.gdp()
            c.indpro()
            c.cpi()
            c.payroll()
            c.housing()
            c.unemployment()
            c.vehicles()
            c.recessionProb()
            c.initialClaims()
            c.institutionalMoney()
            c.retailMoney()

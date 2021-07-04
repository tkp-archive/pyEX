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


class TestRates:
    def test_all(self):
        from pyEX import Client

        c = Client("test")
        with patch("pyEX.common.urls._getIEXCloud"):
            c.thirtyYear()
            c.thirtyYearHistory()
            c.thirtyYearHistoryDF()
            c.twentyYear()
            c.twentyYearHistory()
            c.twentyYearHistoryDF()
            c.tenYear()
            c.tenYearHistory()
            c.tenYearHistoryDF()
            c.sevenYear()
            c.sevenYearHistory()
            c.sevenYearHistoryDF()
            c.fiveYear()
            c.fiveYearHistory()
            c.fiveYearHistoryDF()
            c.threeYear()
            c.threeYearHistory()
            c.threeYearHistoryDF()
            c.twoYear()
            c.twoYearHistory()
            c.twoYearHistoryDF()
            c.oneYear()
            c.oneYearHistory()
            c.oneYearHistoryDF()
            c.sixMonth()
            c.sixMonthHistory()
            c.sixMonthHistoryDF()
            c.threeMonth()
            c.threeMonthHistory()
            c.threeMonthHistoryDF()
            c.oneMonth()
            c.oneMonthHistory()
            c.oneMonthHistoryDF()

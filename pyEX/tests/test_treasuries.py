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


class TestTreasuries:
    def test_all(self):
        from pyEX import Client

        c = Client("test")
        with patch("pyEX.common.urls._getIEXCloud"):
            c.thirtyYear()
            c.thirtyYearDF()
            c.twentyYear()
            c.twentyYearDF()
            c.tenYear()
            c.tenYearDF()
            c.sevenYear()
            c.sevenYearDF()
            c.fiveYear()
            c.fiveYearDF()
            c.threeYear()
            c.threeYearDF()
            c.twoYear()
            c.twoYearDF()
            c.oneYear()
            c.oneYearDF()
            c.sixMonth()
            c.sixMonthDF()
            c.threeMonth()
            c.threeMonthDF()
            c.oneMonth()
            c.oneMonthDF()

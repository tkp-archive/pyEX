# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

# for Coverage
import atexit
import pickle

from mock import MagicMock, patch

atexit.register = MagicMock()
pickle.dump = MagicMock()


class TestCommodities:
    def test_all(self):
        from pyEX import Client

        c = Client("test")
        with patch("pyEX.common.urls._getIEXCloud"):
            c.brent()
            c.brentHistory()
            c.brentHistoryDF()
            c.diesel()
            c.dieselHistory()
            c.dieselHistoryDF()
            c.gasmid()
            c.gasmidHistory()
            c.gasmidHistoryDF()
            c.gasprm()
            c.gasprmHistory()
            c.gasprmHistoryDF()
            c.gasreg()
            c.gasregHistory()
            c.gasregHistoryDF()
            c.heatoil()
            c.heatoilHistory()
            c.heatoilHistoryDF()
            c.jet()
            c.jetHistory()
            c.jetHistoryDF()
            c.natgas()
            c.natgasHistory()
            c.natgasHistoryDF()
            c.propane()
            c.propaneHistory()
            c.propaneHistoryDF()
            c.wti()
            c.wtiHistory()
            c.wtiHistoryDF()

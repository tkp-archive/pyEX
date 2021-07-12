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
            c.brentDF()
            c.diesel()
            c.dieselDF()
            c.gasmid()
            c.gasmidDF()
            c.gasprm()
            c.gasprmDF()
            c.gasreg()
            c.gasregDF()
            c.heatoil()
            c.heatoilDF()
            c.jet()
            c.jetDF()
            c.natgas()
            c.natgasDF()
            c.propane()
            c.propaneDF()
            c.wti()
            c.wtiDF()

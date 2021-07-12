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
            c.fedfunds()
            c.fedfundsDF()
            c.creditcard()
            c.creditcardDF()
            c.cdnj()
            c.cdnjDF()
            c.cdj()
            c.cdjDF()
            c.gdp()
            c.gdpDF()
            c.indpro()
            c.indproDF()
            c.cpi()
            c.cpiDF()
            c.payroll()
            c.payrollDF()
            c.housing()
            c.housingDF()
            c.unemployment()
            c.unemploymentDF()
            c.vehicles()
            c.vehiclesDF()
            c.recessionProb()
            c.recessionProbDF()
            c.initialClaims()
            c.initialClaimsDF()
            c.institutionalMoney()
            c.institutionalMoneyDF()
            c.retailMoney()
            c.retailMoneyDF()

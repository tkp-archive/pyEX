# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

# for Coverage
from mock import patch


class TestEconomic:
    def test_all(self):
        from pyEX import Client

        c = Client("test")
        with patch("pyEX.common._getJsonIEXCloud"), patch("pickle.dump"):
            c.us30()
            c.us15()
            c.us5()
            c.fedfunds()
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

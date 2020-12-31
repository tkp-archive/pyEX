# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

# for Coverage
from mock import MagicMock, patch


class TestAccount:
    def test_account(self):
        from pyEX import Client

        c = Client("sktest")
        with patch("pyEX.account._getJson"):
            c.account()
            c.metadata()

    def test_usage(self):
        from pyEX import Client, PyEXception

        c = Client("sktest")
        with patch("pyEX.account._getJson"):
            c.usage()
            c.usage("messages")
            try:
                c.usage("test")
                assert False
            except PyEXception:
                pass

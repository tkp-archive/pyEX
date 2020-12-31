# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

# for Coverage
from mock import MagicMock, patch

C = "AAPL"


class TestClient:
    def test_client(self):
        from pyEX import Client

        c = Client("test")

    def test_client_notoken(self):
        import os

        from pyEX import Client, PyEXception

        tmp = os.environ.pop("IEX_TOKEN", "")
        try:
            Client()
            assert False
        except PyEXception:
            pass
        os.environ["IEX_TOKEN"] = tmp

# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

# for Coverage
from mock import MagicMock, patch

SYMBOL = "aapl"


class TestAll:
    def test_other(self):
        from pyEX.marketdata.sse import DeepChannelsSSE, _runSSE

        with patch("pyEX.marketdata.sse._streamSSE"):
            # coverage
            _runSSE("test")
            _runSSE("test", symbols=["test"])

            # coverage
            DeepChannelsSSE.options()

    def test_tops(self):
        from pyEX import Client

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            c = Client(version="sandbox")

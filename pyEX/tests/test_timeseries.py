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
import time
from mock import MagicMock, patch

SYMBOL = "aapl"

atexit.register = MagicMock()
pickle.dump = MagicMock()


class TestAll:
    def teardown(self):
        time.sleep(0.1)  # prevent being blocked

    def test_timeseries(self):
        from pyEX import timeSeries

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            timeSeries("NEWS", last=1)

    def test_timeseries_offset(self):
        from pyEX import timeSeries

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            timeSeries("NEWS", offset=1)

    def test_timeseriesDF(self):
        from pyEX import timeSeriesDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(
                return_value={"test": [4], "symbol": ["test"]}
            )
            timeSeriesDF("NEWS", last=1)

    def test_timeseries_subattribute(self):
        from pyEX import Client

        c = Client(version="sandbox")
        c.timeSeries("NEWS", subattribute={"lang": "en"})
        c.timeSeries("NEWS", subattribute=[("lang", "=", "en")])

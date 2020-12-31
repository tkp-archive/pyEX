# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

# for Coverage
import time

from mock import MagicMock, patch

SYMBOL = "aapl"


class TestPoints:
    def teardown(self):
        time.sleep(0.1)  # prevent being blocked

    def test_points(self):
        from pyEX import points

        with patch("requests.get") as mock, patch("pickle.dump"):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            points()
            points("aapl")
            points("aapl", "test")

    def test_pointsDF(self):
        from pyEX import pointsDF

        with patch("requests.get") as mock, patch("pickle.dump"):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            pointsDF("test")

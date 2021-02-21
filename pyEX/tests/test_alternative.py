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
import time

from mock import MagicMock, patch

atexit.register = MagicMock()
pickle.dump = MagicMock()

SYMBOL = "aapl"


class TestAlternative:
    def teardown(self):
        time.sleep(0.1)  # prevent being blocked

    def test_sentiment(self):
        from pyEX import sentiment

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            sentiment("test")

    def test_sentimentDF(self):
        from pyEX import sentimentDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            sentimentDF("test")

    def test_ceoComp(self):
        from pyEX import ceoCompensation

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            ceoCompensation("test")

    def test_ceoCompDF(self):
        from pyEX import ceoCompensationDF

        with patch("requests.get") as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            ceoCompensationDF("test")

# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

import atexit
import pickle
import time

from mock import MagicMock

SYMBOL = "BAC"


atexit.register = MagicMock()
pickle.dump = MagicMock()


class TestMetadata:
    def teardown(self):
        time.sleep(0.1)  # prevent being blocked

    def test_metadata(self):
        from pyEX import Client

        c = Client(version="sandbox")
        # vanilla
        c.queryMetadata("SPLITS")
        # `any`
        c.queryMetadata(None, key="AAPL")

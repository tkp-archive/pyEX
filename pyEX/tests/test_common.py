# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

# for Coverage
from mock import MagicMock, patch


class TestAll:
    def test_getJson(self):
        from pyEX.common import PyEXception, _getJson

        with patch("requests.get") as mock, patch("pickle.dump"):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            _getJson("")

            mock.return_value.status_code = 404
            try:
                _getJson("")
                assert False
            except PyEXception:
                pass

    def test_getJson2(self):
        from pyEX.common import PyEXception, _getJson

        with patch("requests.get") as mock, patch("pickle.dump"):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            _getJson("", "test", "test")

            mock.return_value.status_code = 404
            try:
                _getJson("", "test", "test")
                assert False
            except PyEXception:
                pass

    def test_tryJson(self):
        from pyEX.common import _tryJson

        assert _tryJson("test") == "test"
        assert _tryJson('{"test":"test"}', raw=False) == {"test": "test"}
        assert _tryJson("test", raw=False) == "test"

    def test_wsURL(self):
        from pyEX.common import _wsURL

        _wsURL("test")

    def test_strToList(self):
        from pyEX.common import _strToList

        _strToList("test")

    def test_strCommaSeparatedString(self):
        from pyEX.common import _strCommaSeparatedString

        assert _strCommaSeparatedString(["test", "test2"]) == "test,test2"
        assert _strCommaSeparatedString("test,test2") == "test,test2"

    def test_setProxy(self):
        import pyEX.common as pc

        pc.setProxy("test")
        print(pc._PYEX_PROXIES)
        assert pc._PYEX_PROXIES == "test"
        pc.setProxy(None)

    def test_strOrDate(self):
        from datetime import datetime

        from pyEX.common import PyEXception, _strOrDate

        _strOrDate("test")
        _strOrDate(datetime.now())
        try:
            _strOrDate(5)
            assert False
        except PyEXception:
            pass

    def test_raiseIfNotStr(self):
        from pyEX.common import PyEXception, _raiseIfNotStr

        _raiseIfNotStr("test")
        _raiseIfNotStr(None)
        try:
            _raiseIfNotStr(5)
        except PyEXception:
            pass

    def test_wsclient(self):
        from pyEX.common import WSClient

        ws = WSClient("test")
        ws = WSClient("test", None, print, print, print)

        assert ws.addr == "test"
        assert ws.sendinit is None

        n = ws._Namespace(MagicMock(), MagicMock())
        n.on_connect(None)
        n.on_disconnect(None)
        n.on_message(None)

        with patch("pyEX.common.SocketIO"):
            ws.sendinit = "test"
            ws.run()

    def test_stream(self):
        from pyEX.common import _stream

        with patch("pyEX.common.WSClient"):
            _stream("")

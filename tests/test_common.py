# for Coverage
from mock import patch, MagicMock


class TestAll:
    def setup(self):
        pass
        # setup() before each test method

    def teardown(self):
        pass
        # teardown() after each test method

    @classmethod
    def setup_class(cls):
        pass
        # setup_class() before any methods in this class

    @classmethod
    def teardown_class(cls):
        pass
        # teardown_class() after any methods in this class

    def test_getJson(self):
        from pyEX.common import _getJson, PyEXception
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            _getJson('')

            mock.return_value.status_code = 404
            try:
                _getJson('')
                assert False
            except PyEXception:
                pass

    def test_wsURL(self):
        from pyEX.common import _wsURL
        _wsURL('test')

    def test_strToList(self):
        from pyEX.common import _strToList
        _strToList('test')

    def test_strOrDate(self):
        from pyEX.common import _strOrDate, PyEXception
        from datetime import datetime
        _strOrDate('test')
        _strOrDate(datetime.now())
        try:
            _strOrDate(5)
            assert False
        except PyEXception:
            pass

    def test_raiseIfNotStr(self):
        from pyEX.common import _raiseIfNotStr, PyEXception
        _raiseIfNotStr('test')
        _raiseIfNotStr(None)
        try:
            _raiseIfNotStr(5)
        except PyEXception:
            pass

    def test_wsclient(self):
        from pyEX.common import WSClient
        ws = WSClient('test')
        ws = WSClient('test', None, print, print, print)

        assert ws.addr == 'test'
        assert ws.sendinit is None

        n = ws._Namespace(MagicMock(), MagicMock())
        n.on_connect(None)
        n.on_disconnect(None)
        n.on_message(None)

        with patch('pyEX.common.SocketIO'):
            ws.sendinit = 'test'
            ws.run()

    def test_stream(self):
        from pyEX.common import _stream
        with patch('pyEX.common.WSClient'):
            _stream('')

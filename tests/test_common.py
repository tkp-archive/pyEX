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
        from pyEX.common import _getJson
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            _getJson('')

    def test_wsURL(self):
        from pyEX.common import _wsURL
        _wsURL('test')

    def test_df(self):
        from pyEX.common import _df
        _df({'A': 'B'})

    def test_strToList(self):
        from pyEX.common import _strToList
        _strToList('test')

    def test_raiseIfNotStr(self):
        from pyEX.common import _raiseIfNotStr
        _raiseIfNotStr('test')
        _raiseIfNotStr(None)
        try:
            _raiseIfNotStr(5)
        except:
            pass

    def test_wsclient(self):
        from pyEX.common import WSClient
        WSClient('ws://test')

    def test_stream(self):
        from pyEX.common import _stream
        with patch('pyEX.common.WSClient'):
            _stream('')

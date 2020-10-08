# for Coverage
from mock import patch, MagicMock


class TestAccount:
    def test_account(self):
        from pyEX import Client
        c = Client('sktest')
        with patch('pyEX.account._getJson'):
            c.account()
            c.metadata()

    def test_usage(self):
        from pyEX import Client
        from pyEX import PyEXception
        c = Client('sktest')
        with patch('pyEX.account._getJson'):
            c.usage()
            c.usage('messages')
            try:
                c.usage('test')
                assert False
            except PyEXception:
                pass

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

    def test_markets(self):
        from pyEX import markets
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            markets()

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

    def test_stats(self):
        from pyEX.stats import stats
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            stats()

    def test_recent(self):
        from pyEX.stats import recent
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            recent()

    def test_records(self):
        from pyEX.stats import records
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            records()

    def test_summary(self):
        from datetime import datetime
        from pyEX.stats import summary
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            summary()
            summary('201505')
            summary(datetime.today())

    def test_daily(self):
        from datetime import datetime
        from pyEX.stats import daily
        with patch('requests.get') as mock:
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            daily()
            daily('201505')
            daily(last='5')
            daily(datetime.today())

import pytest
import sys
from mock_demo.bar import Bar

if sys.version_info[0] == 3:  # pragma: no cover
    from unittest.mock import Mock, MagicMock, call, patch, mock_open
else:                         # pragma: no cover
    from mock import Mock, MagicMock, call, patch, mock_open


class BarTestFixture(object):

    def __init__(self):
        self.file_data = "Test Data not from a file"
        self.file_name = "test.txt"
        fake_file = mock_open(read_data=self.file_data)
        with patch("mock_demo.bar.open", fake_file):
            self.bar = Bar(self.file_name)


@pytest.fixture
def bar_fixture():
    fixture = BarTestFixture()
    yield fixture


class TestBar():

    def test_init(self, bar_fixture):
        assert bar_fixture.bar.data == bar_fixture.file_data

    def test_do_process(self, bar_fixture):

        with patch("mock_demo.foo.sleep") as mock_sleep:
            result = bar_fixture.bar.do_process(256)
            assert result == 256 // 2

        mock_lengthy_process = Mock(return_value=False)
        with patch("mock_demo.foo.Foo.lengthy_process", mock_lengthy_process) as mocked_process:
            result = bar_fixture.bar.do_process(1024)
            assert result == -1
            mocked_process.assert_called_with(1024)

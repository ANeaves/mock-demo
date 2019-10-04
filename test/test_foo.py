import pytest
import sys
from mock_demo.foo import Foo

if sys.version_info[0] == 3:  # pragma: no cover
    from unittest.mock import Mock, MagicMock, call, patch
else:                         # pragma: no cover
    from mock import Mock, MagicMock, call, patch


class FooTestFixture(object):

    def __init__(self):
        self.foo = Foo()


@pytest.fixture
def foo_fixture():
    fixture = FooTestFixture()
    yield fixture


class TestFoo():

    def test_init(self, foo_fixture):
        assert foo_fixture.foo.value == 5

    def test_get_platform(self, foo_fixture):
        platform = foo_fixture.foo.get_platform()

        assert platform == "linux"lengthy_process

    def test_windows_get_platform(self, foo_fixture):
        with patch("mock_demo.foo.sys") as mock_sys:
            
            mock_sys.configure_mock(platform="win32")
            mock_sys.getwindowsversion = Mock(return_value="1.3.3.7")

            platform = foo_fixture.foo.get_platform()

            assert platform == "win32 v.1.3.3.7"

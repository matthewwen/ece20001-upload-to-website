import pytest
from ece20001.pages import Page


@pytest.fixture
def _obj():
    return Page()


def test_is_successful(_obj):
    print(_obj)

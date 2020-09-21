import pytest
from ece20001.practice import Practice


@pytest.fixture
def _obj():
    return Practice()


def test_is_successful(_obj):
    print(_obj)

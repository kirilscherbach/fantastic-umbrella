import pytest
from app.utilities.complicated_helpers import Calculator


@pytest.fixture(scope="module")
def calc():
    print("setup!")
    yield Calculator()
    print("here can be your teardown!")

def test_add(calc):
    assert calc.add(2, 3) == 5


def test_long_add(calc):
 result = calc.add(2, 4)
 print("wooow i'm in the middle of a test")
 assert result == 5

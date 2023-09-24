import pytest
from app.utilities.complicated_helpers import Calculator


@pytest.fixture(scope="module")
def calc():
    return Calculator()


@pytest.mark.parametrize(
    "num1, num2, expected_result",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (-2, -2, -4),
        (3.5, 2.5, 6.0),
    ],
)
def test_add(calc, num1, num2, expected_result):
    assert calc.add(num1, num2) == expected_result

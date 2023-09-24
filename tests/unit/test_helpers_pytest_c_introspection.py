import pytest

def test_eq_long_text():
    a = "1" * 100 + "a" + "2" * 100
    b = "1" * 100 + "b" + "2" * 100
    assert a == b



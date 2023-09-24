import pytest
import sys
from app.utilities.helpers import add

@pytest.mark.slow()
def test_marked():
    assert add(2, 3) == 5


@pytest.mark.skip(reason="mismatching types will be supported in next release")
def test_string_addition():
   assert add("2", "3") == 5

#@pytest.mark.skipif(sys.version_info < (3, 0), reason="Doesn't work on Python 2.7")


@pytest.mark.xfail(raises=ValueError, strict=True)
def test_mismatching_types():
    assert add(2, 3) == 5

#@pytest.mark.xfail(raises=ValueError) - will fail, because the error is unexpected
#@pytest.mark.xfail(run=False) - will not run the test

#@pytest.mark.xfail(strict=True) will fail if the test passed, but default is False


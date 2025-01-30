from homework.homework1.third_from_the_end import define
import pytest


@pytest.mark.parametrize("x, except_result", [
    (8804, 8), (9531, 5), (2132, 1)])
def test_define(x, except_result):
    assert define(x) == except_result


@pytest.mark.parametrize("x", [54, 99999, -100])
def test_define_out_of_range(x):
    with pytest.raises(ValueError, match="out of range"):
        define(x)

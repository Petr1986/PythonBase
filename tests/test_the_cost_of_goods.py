from homework.homework1.the_cost_of_goods import cost
import pytest


@pytest.mark.parametrize("k, except_result", [
    (2144, (21, 44)), (1825, (18, 25)), (3983, (39, 83))])
def test_cost(k, except_result):
    assert cost(k) == except_result


@pytest.mark.parametrize("k", [-12, 10001, 999999])
def test_cost_out_of_range(k):
    with pytest.raises(ValueError, match="out of range"):
        cost(k)

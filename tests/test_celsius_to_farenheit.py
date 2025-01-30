from homework.homework1.celsius_to_fahrenheit import conversion
import pytest


@pytest.mark.parametrize("x, expected_result", [
    (-21, -5), (4, 39), (-11, 12), (43, 109)])
def test_conversion(x, expected_result):
    assert conversion(x) == expected_result


@pytest.mark.parametrize("x", [-300, 1500])
def test_conversation_out_of_range(x):
    with pytest.raises(ValueError, match=f"Temperature {x} is out of range"):
        conversion(x)

from homework1.celsius_to_fahrenheit import conversion
import pytest

@pytest.mark.parametrize("x, expected_result", [(-21, -5),
                                                (4, 39),
                                                (-11, 12),
                                                (43, 109)])
def test_conversion(x, expected_result):
    assert conversion(x) == expected_result

def test_conversation_out_of_range():
    with pytest.raises(ValueError, match=r"Temperature .* is out of range"):
        conversion(-300)

    with pytest.raises(ValueError, match=r"Temperature .* is out of range"):
        conversion(1500)

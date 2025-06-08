import pytest
from ..solutions.s010_roman_to_integer import (
    Solution,
)

TEST_CASES = [
    # User-provided cases
    ({"s": "III"}, 3),
    ({"s": "LVIII"}, 58),
    ({"s": "MCMXCIV"}, 1994),
    # All subtractive cases
    ({"s": "IV"}, 4),
    ({"s": "IX"}, 9),
    ({"s": "XL"}, 40),
    ({"s": "XC"}, 90),
    ({"s": "CD"}, 400),
    ({"s": "CM"}, 900),
    # Single characters
    ({"s": "I"}, 1),
    ({"s": "V"}, 5),
    ({"s": "X"}, 10),
    ({"s": "L"}, 50),
    ({"s": "C"}, 100),
    ({"s": "D"}, 500),
    ({"s": "M"}, 1000),
    # Other valid combinations
    ({"s": "VI"}, 6),  # Standard addition
    ({"s": "MMXXIII"}, 2023), # A more recent year
    ({"s": "CDXLIV"}, 444), # Multiple subtractive rules
    # A long Roman numeral without subtraction
    ({"s": "MMMDCCCLXXXVIII"}, 3888),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_romanToInt(inputs_dict, expected_output):
    """
    Tests the romanToInt method of the Solution class.
    """
    solver = Solution()
    actual_output = solver.romanToInt(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for s='{inputs_dict['s']}'. "
        f"Expected {expected_output}, got {actual_output}"
    )

import pytest
from ..solutions.s012_palindrome_number import Solution


TEST_CASES = [
    ({"x": 121}, True),
    ({"x": -121}, False),
    ({"x": 10}, False),
    # Edge cases
    ({"x": 0}, True),
    ({"x": 1}, True),
    ({"x": 11}, True),
    ({"x": 1001}, True),
    ({"x": 1000021}, False),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_isPalindrome(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.isPalindrome(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


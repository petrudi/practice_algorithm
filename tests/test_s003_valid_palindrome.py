import pytest
from ..solutions.s003_valid_palindrome import Solution

TEST_CASES = [
    ({"s": "A man, a plan, a canal: Panama"}, True),
    ({"s": "race a car"}, False),
    ({"s": " "}, True),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_isPalindrome(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.isPalindrome(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )

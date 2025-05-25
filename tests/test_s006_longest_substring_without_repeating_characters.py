import pytest
from ..solutions.s006_longest_substring_without_repeating_characters import Solution

TEST_CASES = [({"s": "abcabcbb"}, 3)]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_lengthOfLongestSubstring(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.lengthOfLongestSubstring(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )

import pytest
from ..solutions.s008_longest_common_prefix import Solution

# Test cases, including the ones you provided and some common edge cases
# Based on LeetCode constraints: strs.length >= 1
TEST_CASES = [
    # User-provided cases
    ({"strs": ["flower", "flow", "flight"]}, "fl"),
    ({"strs": ["dog", "racecar", "car"]}, ""),
    # Additional common cases
    ({"strs": [""]}, ""),  # List with one empty string
    ({"strs": ["a"]}, "a"),  # List with one non-empty string
    ({"strs": ["", "b"]}, ""),  # First string is empty
    ({"strs": ["a", ""]}, ""),  # Later string is empty
    ({"strs": ["abc", "abd", "abe"]}, "ab"),  # Standard common prefix
    ({"strs": ["cir", "car"]}, "c"),  # Shorter common prefix
    ({"strs": ["apple", "apply", "ape"]}, "ap"),
    (
        {"strs": ["interspecies", "interstellar", "interstate"]},
        "inters",
    ),  # Longer common prefix
    ({"strs": ["prefix", "suffix"]}, ""),  # No common prefix at all
    ({"strs": ["", "", ""]}, ""),  # All strings are empty
    ({"strs": ["abc", "abc", "abc"]}, "abc"),  # All strings are identical
    ({"strs": ["abab", "ab", "aba"]}, "ab"),  # Prefix varies in length
    (
        {"strs": ["reflower", "flow", "flight"]},
        "",
    ),  # No common prefix due to first char mismatch with others
    ({"strs": ["aa", "a"]}, "a"),  # One string is a prefix of another
    ({"strs": ["c", "c"]}, "c"),  # List of two identical short strings
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_longestCommonPrefix_Solution(inputs_dict, expected_output):
    """
    Tests the longestCommonPrefix method of the Solution class.
    """
    solver = Solution()
    actual_output = solver.longestCommonPrefix(**inputs_dict)
    assert actual_output == expected_output, (
        f"Solution: Failed for input {inputs_dict['strs']}. "
        f"Expected '{expected_output}', got '{actual_output}'"
    )

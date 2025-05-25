import pytest
from ..solutions.s009_find_the_index_of_the_first_occurrence_in_a_string import (
    Solution,
)  # Adjust module path as needed

# Test cases, including the ones you provided and some common edge cases
TEST_CASES = [
    # User-provided cases
    ({"haystack": "sadbutsad", "needle": "sad"}, 0),
    ({"haystack": "hello", "needle": "ll"}, 2),
    # Additional common cases
    ({"haystack": "leetcode", "needle": "leeto"}, -1),  # Needle not found
    ({"haystack": "aaaaa", "needle": "bba"}, -1),  # Needle not found
    ({"haystack": "hello", "needle": ""}, 0),  # Empty needle returns 0
    ({"haystack": "", "needle": "a"}, -1),  # Empty haystack, non-empty needle
    ({"haystack": "", "needle": ""}, 0),  # Empty haystack, empty needle
    ({"haystack": "abc", "needle": "abc"}, 0),  # Needle is the same as haystack
    ({"haystack": "abc", "needle": "c"}, 2),  # Needle at the end
    ({"haystack": "mississippi", "needle": "issi"}, 1),  # First occurrence
    ({"haystack": "mississippi", "needle": "issip"}, 4),  # Further occurrence
    ({"haystack": "mississippi", "needle": "pi"}, 9),  # At the end
    ({"haystack": "abc", "needle": "abcd"}, -1),  # Needle longer than haystack
    ({"haystack": "a", "needle": "a"}, 0),  # Single character match
    ({"haystack": "b", "needle": "a"}, -1),  # Single character mismatch
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_strStr(inputs_dict, expected_output):
    """
    Tests the strStr method of the Solution class.
    """
    solver = Solution()
    actual_output = solver.strStr(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for haystack='{inputs_dict['haystack']}', needle='{inputs_dict['needle']}'. "
        f"Expected {expected_output}, got {actual_output}"
    )

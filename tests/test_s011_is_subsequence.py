import pytest
from ..solutions.s011_is_subsequence import Solution


TEST_CASES = [
    ({"s": "abc", "t": "ahbgdc"}, True),
    ({"s": "axc", "t": "ahbgdc"}, False),
    # Edge cases
    ({"s": "", "t": ""}, True),
    ({"s": "", "t": "ahbgdc"}, True),
    ({"s": "a", "t": ""}, False),
    ({"s": "aaaa", "t": "aaaaaaaa"}, True),
    ({"s": "aaaa", "t": "aaabaaaa"}, True),
    ({"s": "abc", "t": "abc"}, True),
    ({"s": "abc", "t": "acb"}, False),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_isSubsequence(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.isSubsequence(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


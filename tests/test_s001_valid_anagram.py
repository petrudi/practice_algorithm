import pytest
from ..solutions.s001_valid_anagram import Solution

TEST_CASES = [
    ({"s": "anagram", "t": "nagaram"}, True),
    ({"s": "rat", "t": "car"}, False),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_isAnagram(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.isAnagram(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )

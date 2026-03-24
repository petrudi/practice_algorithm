import pytest
from ..solutions.s028_ransom_note import Solution


TEST_CASES = [
    ({"ransomNote": "a", "magazine": "b"}, False),
    ({"ransomNote": "aa", "magazine": "ab"}, False),
    ({"ransomNote": "aa", "magazine": "aab"}, True),
    # Edge cases
    ({"ransomNote": "", "magazine": ""}, True),
    ({"ransomNote": "", "magazine": "abc"}, True),
    ({"ransomNote": "abc", "magazine": "abc"}, True),
    ({"ransomNote": "aaaaa", "magazine": "aaa"}, False),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_canConstruct(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.canConstruct(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


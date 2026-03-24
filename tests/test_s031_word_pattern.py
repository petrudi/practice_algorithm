import pytest
from ..solutions.s031_word_pattern import Solution


TEST_CASES = [
    ({"pattern": "abba", "s": "dog cat cat dog"}, True),
    ({"pattern": "abba", "s": "dog cat cat fish"}, False),
    ({"pattern": "aaaa", "s": "dog cat cat dog"}, False),
    ({"pattern": "abba", "s": "dog dog dog dog"}, False),
    # Edge cases
    ({"pattern": "", "s": ""}, True),
    ({"pattern": "a", "s": ""}, False),
    ({"pattern": "ab", "s": "dog"}, False),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_wordPattern(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.wordPattern(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


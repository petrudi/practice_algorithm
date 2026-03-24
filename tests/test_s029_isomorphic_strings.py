import pytest
from ..solutions.s029_isomorphic_strings import Solution


TEST_CASES = [
    ({"s": "egg", "t": "add"}, True),
    ({"s": "foo", "t": "bar"}, False),
    ({"s": "paper", "t": "title"}, True),
    # Edge cases
    ({"s": "", "t": ""}, True),
    ({"s": "ab", "t": "aa"}, False),
    ({"s": "aa", "t": "ab"}, False),
    ({"s": "badc", "t": "baba"}, False),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_isIsomorphic(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.isIsomorphic(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


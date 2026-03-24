import pytest
from ..solutions.s016_valid_parentheses import Solution


TEST_CASES = [
    ({"s": "()"}, True),
    ({"s": "()[]{}"}, True),
    ({"s": "(]"}, False),
    # Edge cases
    ({"s": ""}, True),
    ({"s": "("}, False),
    ({"s": "([)]"}, False),
    ({"s": "{[]}"}, True),
    ({"s": "(((((())))))"}, True),
    ({"s": "])"}, False),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_isValid(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.isValid(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


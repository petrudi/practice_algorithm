import pytest
from ..solutions.s019_reverse_words_in_a_string import Solution1, Solution2, Solution3


TEST_CASES = [
    ({"s": "the sky is blue"}, "blue is sky the"),
    ({"s": "  hello world  "}, "world hello"),
    ({"s": "a good   example"}, "example good a"),
    # Edge cases
    ({"s": ""}, ""),
    ({"s": "     "}, ""),
    ({"s": "single"}, "single"),
    ({"s": "  multiple   spaces   here "}, "here spaces multiple"),
]


@pytest.mark.parametrize("solver_cls", [Solution1, Solution2, Solution3])
@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_reverseWords(solver_cls, inputs_dict, expected_output):
    solver = solver_cls()
    actual_output = solver.reverseWords(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict} using {solver_cls.__name__}. "
        f"Expected {expected_output}, got {actual_output}"
    )


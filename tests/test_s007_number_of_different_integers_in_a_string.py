import pytest
from ..solutions.s007_number_of_different_integers_in_a_string import Solution

TEST_CASES = [
    ({"word": "a123bc34d8ef34"}, 3),
    ({"word": "leet1234code234"}, 2),
    ({"word": "a1b01c001"}, 1),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_numDifferentIntegers(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.numDifferentIntegers(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )

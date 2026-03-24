import pytest
from ..solutions.s032_happy_number import Solution


TEST_CASES = [
    ({"n": 19}, True),
    ({"n": 2}, False),
    # Edge cases
    ({"n": 1}, True),
    ({"n": 7}, True),
    ({"n": 20}, False),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_isHappy(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.isHappy(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


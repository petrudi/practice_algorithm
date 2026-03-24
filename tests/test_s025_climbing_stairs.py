import pytest
from ..solutions.s025_climbing_stairs import Solution


TEST_CASES = [
    ({"n": 1}, 1),
    ({"n": 2}, 2),
    ({"n": 3}, 3),
    ({"n": 4}, 5),
    ({"n": 5}, 8),
    # A slightly larger case
    ({"n": 10}, 89),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_climbStairs(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.climbStairs(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


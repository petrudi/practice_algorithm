import pytest
from ..solutions.s004_container_with_most_water import Solution

TEST_CASES = [({"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}, 49)]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_maxArea(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.maxArea(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )

import pytest
from ..solutions.s023_two_sum_ii_input_array_is_sorted import Solution


TEST_CASES = [
    ({"numbers": [2, 7, 11, 15], "target": 9}, [1, 2]),
    ({"numbers": [2, 3, 4], "target": 6}, [1, 3]),
    ({"numbers": [-1, 0], "target": -1}, [1, 2]),
    # Edge cases
    ({"numbers": [0, 0, 3, 4], "target": 0}, [1, 2]),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_twoSum(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.twoSum(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


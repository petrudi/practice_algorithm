import pytest
from ..solutions.s020_minimum_size_subarray_sum import Solution


TEST_CASES = [
    ({"target": 7, "nums": [2, 3, 1, 2, 4, 3]}, 2),
    ({"target": 4, "nums": [1, 4, 4]}, 1),
    ({"target": 11, "nums": [1, 1, 1, 1, 1, 1, 1, 1]}, 0),
    # Edge cases
    ({"target": 1, "nums": [1]}, 1),
    ({"target": 15, "nums": [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]}, 2),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_minSubArrayLen(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.minSubArrayLen(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


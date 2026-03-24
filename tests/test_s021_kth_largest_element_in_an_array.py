import pytest
from ..solutions.s021_kth_largest_element_in_an_array import Solution


TEST_CASES = [
    ({"nums": [3, 2, 1, 5, 6, 4], "k": 2}, 5),
    ({"nums": [3, 2, 3, 1, 2, 4, 5, 5, 6], "k": 4}, 4),
    # Edge cases
    ({"nums": [1], "k": 1}, 1),
    ({"nums": [-1, -2, -3, -4], "k": 1}, -1),
    ({"nums": [-1, -2, -3, -4], "k": 4}, -4),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_findKthLargest(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.findKthLargest(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


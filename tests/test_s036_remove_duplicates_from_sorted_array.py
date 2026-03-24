import pytest
from ..solutions.s036_remove_duplicates_from_sorted_array import Solution


TEST_CASES = [
    ({"nums": [1, 1, 2]}, (2, [1, 2])),
    ({"nums": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]}, (5, [0, 1, 2, 3, 4])),
    # Edge cases
    ({"nums": []}, (0, [])),
    ({"nums": [1]}, (1, [1])),
    ({"nums": [1, 1, 1]}, (1, [1])),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_removeDuplicates(inputs_dict, expected_output):
    solver = Solution()
    nums = list(inputs_dict["nums"])
    k = solver.removeDuplicates(nums=nums)
    expected_k, expected_prefix = expected_output
    actual_output = (k, nums[:k])
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


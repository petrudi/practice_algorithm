import pytest
from ..solutions.s022_two_sum import Solution


def is_valid_two_sum(nums, target, ans):
    if ans is None:
        return False
    i, j = ans
    if i == j:
        return False
    if not (0 <= i < len(nums) and 0 <= j < len(nums)):
        return False
    return nums[i] + nums[j] == target


TEST_CASES = [
    ({"nums": [2, 7, 11, 15], "target": 9}, True),
    ({"nums": [3, 2, 4], "target": 6}, True),
    ({"nums": [3, 3], "target": 6}, True),
    # Edge cases
    ({"nums": [-3, 4, 3, 90], "target": 0}, True),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_twoSum(inputs_dict, expected_output):
    solver = Solution()
    ans = solver.twoSum(**inputs_dict)
    actual_output = is_valid_two_sum(inputs_dict["nums"], inputs_dict["target"], ans)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output} with ans={ans}"
    )


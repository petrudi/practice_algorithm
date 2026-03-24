import pytest
from ..solutions.s035_merge_sorted_array import Solution


TEST_CASES = [
    (
        {"nums1": [1, 2, 3, 0, 0, 0], "m": 3, "nums2": [2, 5, 6], "n": 3},
        [1, 2, 2, 3, 5, 6],
    ),
    ({"nums1": [1], "m": 1, "nums2": [], "n": 0}, [1]),
    ({"nums1": [0], "m": 0, "nums2": [1], "n": 1}, [1]),
    # Edge cases
    ({"nums1": [2, 0], "m": 1, "nums2": [1], "n": 1}, [1, 2]),
    ({"nums1": [-1, 0, 0, 3, 3, 3, 0, 0, 0], "m": 6, "nums2": [1, 2, 2], "n": 3}, [-1, 0, 0, 1, 2, 2, 3, 3, 3]),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_merge(inputs_dict, expected_output):
    solver = Solution()
    nums1 = list(inputs_dict["nums1"])
    solver.merge(nums1=nums1, m=inputs_dict["m"], nums2=inputs_dict["nums2"], n=inputs_dict["n"])
    actual_output = nums1
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


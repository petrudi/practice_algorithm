import pytest
from ..solutions.s005_contains_duplicate_ii import Solution

TEST_CASES = [
    ({"k": 3, "nums": [1, 2, 3, 1]}, True),
    ({"k": 1, "nums": [1, 0, 1, 1]}, True),
    ({"k": 2, "nums": [1, 2, 3, 1, 2, 3]}, False),
    ({"k": 2, "nums": [99, 99]}, True),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_containsNearbyDuplicate(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.containsNearbyDuplicate(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )

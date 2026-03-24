import pytest
from ..solutions.s013_search_insert_position import Solution


TEST_CASES = [
    ({"nums": [1, 3, 5, 6], "target": 5}, 2),
    ({"nums": [1, 3, 5, 6], "target": 2}, 1),
    ({"nums": [1, 3, 5, 6], "target": 7}, 4),
    # Edge cases
    ({"nums": [1, 3, 5, 6], "target": 0}, 0),
    ({"nums": [1], "target": 1}, 0),
    ({"nums": [1], "target": 2}, 1),
    ({"nums": [1, 3, 5, 6], "target": 6}, 3),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_searchInsert(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.searchInsert(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


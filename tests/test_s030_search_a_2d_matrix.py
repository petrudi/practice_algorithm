import pytest
from ..solutions.s030_search_a_2d_matrix import Solution


TEST_CASES = [
    ({"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], "target": 3}, True),
    ({"matrix": [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], "target": 13}, False),
    ({"matrix": [[1, 3]], "target": 3}, True),
    # Edge cases
    ({"matrix": [[1]], "target": 1}, True),
    ({"matrix": [[1]], "target": 2}, False),
    ({"matrix": [[1, 3, 5]], "target": 5}, True),
    ({"matrix": [[1], [3], [5]], "target": 3}, True),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_searchMatrix(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.searchMatrix(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


import pytest
from ..solutions.s014_convert_sorted_array_to_binary_search_tree import Solution


def level_order_values(root):
    # Reuse the solution's level-order behavior to match expected arrays.
    return Solution().level_order(root, [])


TEST_CASES = [
    ({"nums": [-10, -3, 0, 5, 9]}, [0, -3, 9, -10, None, 5]),
    ({"nums": [1, 3]}, [3, 1]),
    # Edge cases
    ({"nums": []}, []),
    ({"nums": [0]}, [0]),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_sortedArrayToBST(inputs_dict, expected_output):
    solver = Solution()
    root = solver.sortedArrayToBST(**inputs_dict)
    actual_output = level_order_values(root) if root is not None else []
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


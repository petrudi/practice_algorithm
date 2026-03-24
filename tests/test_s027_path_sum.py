import pytest
from ..solutions.s027_path_sum import Solution, TreeNode


def build_tree_level_order(values):
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kid = 1
    for i in range(len(nodes)):
        if nodes[i] is None:
            continue
        if kid < len(nodes):
            nodes[i].left = nodes[kid]
            kid += 1
        if kid < len(nodes):
            nodes[i].right = nodes[kid]
            kid += 1
    return nodes[0]


TEST_CASES = [
    (
        {"root": build_tree_level_order([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), "targetSum": 22},
        True,
    ),
    ({"root": build_tree_level_order([1, 2, 3]), "targetSum": 5}, False),
    ({"root": None, "targetSum": 0}, False),
    # Edge cases
    ({"root": build_tree_level_order([1]), "targetSum": 1}, True),
    ({"root": build_tree_level_order([1]), "targetSum": 2}, False),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_hasPathSum(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.hasPathSum(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


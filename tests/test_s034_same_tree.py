import pytest
from ..solutions.s034_same_tree import Solution, TreeNode


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
        {
            "p": build_tree_level_order([1, 2, 3]),
            "q": build_tree_level_order([1, 2, 3]),
        },
        True,
    ),
    (
        {
            "p": build_tree_level_order([1, 2]),
            "q": build_tree_level_order([1, None, 2]),
        },
        False,
    ),
    (
        {
            "p": build_tree_level_order([1, 2, 1]),
            "q": build_tree_level_order([1, 1, 2]),
        },
        False,
    ),
    # Edge cases
    ({"p": None, "q": None}, True),
    ({"p": build_tree_level_order([0]), "q": None}, False),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_isSameTree(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.isSameTree(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


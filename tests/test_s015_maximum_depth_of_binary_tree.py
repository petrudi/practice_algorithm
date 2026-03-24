import pytest
from ..solutions.s015_maximum_depth_of_binary_tree import Solution1, Solution2, TreeNode


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
    ({"root": build_tree_level_order([3, 9, 20, None, None, 15, 7])}, 3),
    ({"root": build_tree_level_order([1, None, 2])}, 2),
    ({"root": None}, 0),
    ({"root": build_tree_level_order([0])}, 1),
]


@pytest.mark.parametrize("solver_cls", [Solution1, Solution2])
@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_maxDepth(solver_cls, inputs_dict, expected_output):
    solver = solver_cls()
    actual_output = solver.maxDepth(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict} using {solver_cls.__name__}. "
        f"Expected {expected_output}, got {actual_output}"
    )


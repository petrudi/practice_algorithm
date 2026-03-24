import pytest
from ..solutions.s018_linked_list_cycle import ListNode, Solution1, Solution2


def build_list(values, pos):
    """
    Builds a linked list from values. If pos >= 0, tail points to node at pos.
    Returns the head node.
    """
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0]


TEST_CASES = [
    ({"head": build_list([3, 2, 0, -4], 1)}, True),
    ({"head": build_list([1, 2], 0)}, True),
    ({"head": build_list([1], -1)}, False),
    # Edge cases
    ({"head": None}, False),
    ({"head": build_list([1, 2, 3], -1)}, False),
]


@pytest.mark.parametrize("solver_cls", [Solution1, Solution2])
@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_hasCycle(solver_cls, inputs_dict, expected_output):
    solver = solver_cls()
    actual_output = solver.hasCycle(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict} using {solver_cls.__name__}. "
        f"Expected {expected_output}, got {actual_output}"
    )


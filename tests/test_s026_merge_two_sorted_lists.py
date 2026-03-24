import pytest
from ..solutions.s026_merge_two_sorted_lists import ListNode, Solution


def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


TEST_CASES = [
    ({"list1": build_list([1, 2, 4]), "list2": build_list([1, 3, 4])}, [1, 1, 2, 3, 4, 4]),
    ({"list1": build_list([]), "list2": build_list([])}, []),
    ({"list1": build_list([]), "list2": build_list([0])}, [0]),
    # Edge cases
    ({"list1": build_list([5]), "list2": build_list([1, 2, 3])}, [1, 2, 3, 5]),
    ({"list1": build_list([1, 2, 3]), "list2": build_list([4])}, [1, 2, 3, 4]),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_mergeTwoLists(inputs_dict, expected_output):
    solver = Solution()
    merged = solver.mergeTwoLists(**inputs_dict)
    actual_output = to_list(merged)
    assert actual_output == expected_output, (
        f"Failed for input lists. Expected {expected_output}, got {actual_output}"
    )


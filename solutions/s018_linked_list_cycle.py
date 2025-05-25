# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:  # time: O(N), space: O(N)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next

        return False


class Solution2:  # time: O(N), space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == "visited":
                return True
            head.val = "visited"
            head = head.next

        return False

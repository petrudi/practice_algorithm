# https://leetcode.com/problems/linked-list-cycle/


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1: # time: O(N), space: O(N)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        
        return False

class Solution2: # time: O(N), space: O(1)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        while cur:
            if cur.val == "visited": return True
            cur.val = "visited"
            cur = cur.next
        
        return False

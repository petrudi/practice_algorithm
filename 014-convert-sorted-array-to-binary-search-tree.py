# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional
from collections import deque


TEST_CASES = [
        ({"nums": [-10,-3,0,5,9]}, [0,-3,9,-10,None,5]),
        ({"nums": [1,3]}, [3,1]),
]


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({str(self.val)})"
        
    def __str__(self):
        return str(self.val)

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0 :
            return None

        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


    def level_order(self, node: TreeNode, output: List[int]):
        if node is None:
            return

        q = deque()
        q.append(node)

        while q and any(q):
            node = q.popleft()
            if node:
                output.append(node.val)
            else:
                output.append(None)
            if node is None:
                continue
            if node.left:
                q.append(node.left)
            else:
                q.append(None)
            
            if node.right:
                q.append(node.right)
            else:
                q.append(None)

        return output


if __name__ == "__main__":
    for inputs,expected_output in TEST_CASES:
        actual_output = Solution().level_order(Solution().sortedArrayToBST(**inputs), [])
        assert actual_output == expected_output, f"{inputs=}, {actual_output=}, {expected_output=}"

    print("all passed!")

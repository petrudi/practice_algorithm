# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stk = [(root, 1)] # (node, depth)
        max_depth = 0
        while stk:
            node, depth= stk.pop()
            max_depth = max(max_depth, depth)
            if node.right: stk.append((node.right, depth + 1))
            if node.left: stk.append((node.left, depth + 1))
        return max_depth


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        max_depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        return max_depth

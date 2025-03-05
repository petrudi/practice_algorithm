# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = 0
        while p1 < len(nums) and p2 < len(nums):
            nums[p1] = nums[p2]
            while p2 < len(nums) and nums[p2] == nums[p1]:
                p2 += 1
            p1 += 1
        return p1

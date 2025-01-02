# https://leetcode.com/problems/minimum-size-subarray-sum/


from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int: # Time: O(n), Space: O(1)
        l = s = 0
        min_length = float('inf')

        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                min_length = min(min_length, r-l+1)
                s -= nums[l]
                l += 1
            
        return min_length if min_length<float('inf') else 0

# https://leetcode.com/problems/summary-ranges/


from typing import List


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]
        a = nums[0]
        b = nums[0]
        output: list[str] = []
        for idx, num in enumerate(nums[1:], start=1):
            if num - b == 1:
                b = num
            elif num - b > 1:
                if a == b:
                    output.append(f"{a}")
                else:
                    output.append(f"{a}->{b}")
                a = num
                b = num
            if idx == len(nums) - 1:
                if a == b:
                    output.append(f"{a}")
                else:
                    output.append(f"{a}->{b}")

        return output


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        r = 0
        while r < len(nums):
            l = r
            while r < len(nums) - 1 and nums[r + 1] - nums[r] == 1:
                r += 1
            if l == r:
                output.append(f"{nums[l]}")
            else:
                output.append(f"{nums[l]}->{nums[r]}")
            r += 1
        return output


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        l = 0
        while l < len(nums):
            r = l
            while r < len(nums) - 1 and nums[r + 1] - nums[r] == 1:
                r += 1
            if l == r:
                output.append(f"{nums[l]}")
            else:
                output.append(f"{nums[l]}->{nums[r]}")
            l = r + 1
        return output

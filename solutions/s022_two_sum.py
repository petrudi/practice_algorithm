class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for idx, num in enumerate(nums):
            h[num] = idx

        for idx, num in enumerate(nums):
            looking_for = target - num
            if looking_for in h and idx != h[looking_for]:
                return idx, h[looking_for]

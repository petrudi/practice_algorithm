from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0 , len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if target == s:
                return [l + 1, r + 1]
            elif target < s:
                r -= 1
            else:
                l += 1

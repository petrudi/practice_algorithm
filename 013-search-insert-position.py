# https://leetcode.com/problems/search-insert-position/
from typing import List

TEST_CASES = [
        ({"nums": [1,3,5,6], "target": 5}, 2),
        ({"nums": [1,3,5,6], "target": 2}, 1),
        ({"nums": [1,3,5,6], "target": 7}, 4),
]


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid - 1
            elif target> nums[mid]:
                left = mid + 1
            else:
                return mid

        return left


if __name__ == "__main__":
    for inputs,expected_output in TEST_CASES:
        actual_output = Solution().searchInsert(**inputs)
        assert actual_output == expected_output, f"{inputs=}, {actual_output=}, {expected_output=}"

    print("all passed!")

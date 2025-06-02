# https://leetcode.com/problems/contains-duplicate-ii/


from typing import List


class Solution1:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False

        if len(nums) == 1:
            return False

        # left and right pointers that define the sliding window, up to size k
        left = 0
        right = min(k, len(nums) - 1)

        # Initialize the sliding window
        window_elements = nums[left : right + 1]
        window_size = len(window_elements)
        window_set = set(window_elements)
        while right < len(nums):
            has_duplicates = len(window_set) != window_size
            if has_duplicates:
                return True

            # If we reached the end of the array, break out of the loop
            if right + 1 == len(nums):
                break

            # update the window
            window_set.remove(nums[left])
            window_set.add(nums[right + 1])

            # move the window one step to the right
            left += 1
            right += 1

        return False


class Solution2:
    def containsNearbyDuplicate(
        self, nums: List[int], k: int
    ) -> bool:  # Time: O(n), space O(1)
        l = 0
        memo = set()
        for r in range(len(nums)):
            # slide the window
            # check if there is any duplicate in window
            if nums[r] in memo:
                return True

            memo.add(nums[r])

            if w := r - l + 1 > k:
                memo.remove(nums[l])
                l += 1

            r += 1
        return False


class Solution:
    def containsNearbyDuplicate(
        self, nums: List[int], k: int
    ) -> bool:  # Time: O(n), space O(1)
        l = r = 0
        memo = set()
        while r < len(nums):
            while r - l <= k and r < len(nums):
                if nums[r] in memo:
                    return True
                memo.add(nums[r])
                r += 1
            memo.remove(nums[l])
            l += 1

        return False


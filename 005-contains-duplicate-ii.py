# https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k == 0:
            return False

        if len(nums) == 1:
            return False

        # left and right pointers that define the sliding window, up to size k
        left = 0
        right = min(k,len(nums)-1)
        
        # Initialize the sliding window
        window_elements = nums[left:right+1]
        window_size = len(window_elements)
        window_set = set(window_elements)
        while right < len(nums):
            has_duplicates = len(window_set)!=window_size
            if has_duplicates:
                return True

            # If we reached the end of the array, break out of the loop
            if right+1 == len(nums):
                break
            
            # update the window
            window_set.remove(nums[left])
            window_set.add(nums[right+1])

            # move the window one step to the right
            left+=1
            right+=1

        return False


if __name__ == "__main__":
    test_cases = [
            ({"nums": [1,2,3,1], "k": 3}, True),
            ({"nums": [1,0,1,1], "k": 1}, True),
            ({"nums": [1,2,3,1,2,3], "k": 2}, False),
            ({"nums": [99,99], "k": 2}, True),
    ]
    for inputs,expected_output in test_cases:
        actual_output = Solution().containsNearbyDuplicate(**inputs)
        assert actual_output == expected_output, f"{inputs=}, {actual_output=}, {expected_output=}"

    print("all passed!")


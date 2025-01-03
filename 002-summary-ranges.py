# https://leetcode.com/problems/summary-ranges/


from typing import List


class Solution1:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [f"{nums[0]}"]
        a = nums[0]
        b = nums[0]
        output: list[str] = []
        for idx,num in enumerate(nums[1:], start=1):
            if num - b == 1:
                b = num
            elif num - b > 1:
                if a == b:
                    output.append(f"{a}")
                else:
                    output.append(f"{a}->{b}")
                a = num
                b = num
            if idx==len(nums)-1:
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
            while r < len(nums) - 1 and nums[r+1] - nums[r] == 1:
                r += 1
            if l == r:
                output.append(f"{nums[l]}")
            else:
                output.append(f"{nums[l]}->{nums[r]}")
            r += 1
        return output


if __name__ == "__main__":
    test_cases = [
        ({"nums": [0,1,2,4,5,7]}, ["0->2","4->5","7"]),
        ({"nums": [0,2,3,4,6,8,9]}, ["0","2->4","6","8->9"]),
    ]
    for inputs,expected_output in test_cases:
        actual_output = Solution().summaryRanges(**inputs)
        assert actual_output == expected_output, f"{actual_output=}, {expected_output=}"

    print("all passed!")

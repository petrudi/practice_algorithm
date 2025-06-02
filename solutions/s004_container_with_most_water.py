# https://leetcode.com/problems/container-with-most-water/

calc_area = lambda i, j, h: (j - i) * h


class Solution:
    def maxArea(self, height: list[int]) -> int:
        optimum_output = 0
        if len(height) in [0, 1]:
            return optimum_output

        l = 0
        r = len(height) - 1
        while l < r:
            min_height = min(height[l], height[r])
            area = calc_area(l, r, min_height)
            optimum_output = max(area, optimum_output)
            if height[l] < height[r]:
                l += 1
                continue
            r -= 1

        return optimum_output



# https://leetcode.com/problems/container-with-most-water/

calc_area = lambda i, j, h: (j - i) * h


class Solution:
    def maxArea(self, height: list[int]) -> int:
        optimum_output = 0
        if len(height) in [0, 1]:
            return optimum_output

        p1 = 0
        p2 = len(height) - 1
        while p1 < p2:
            min_height = min(height[p1], height[p2])
            area = calc_area(p1, p2, min_height)
            optimum_output = max(area, optimum_output)
            if height[p1] < height[p2]:
                p1 += 1
                continue
            p2 -= 1

        return optimum_output


if __name__ == "__main__":
    test_cases = [
        ({"height": [1, 8, 6, 2, 5, 4, 8, 3, 7]}, 49),
    ]
    for inputs, expected_output in test_cases:
        actual_output = Solution().maxArea(**inputs)
        assert actual_output == expected_output, (
            f"{inputs=}, {actual_output=}, {expected_output=}"
        )

    print("all passed!")

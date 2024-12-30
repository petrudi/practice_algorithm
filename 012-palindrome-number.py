# https://leetcode.com/problems/palindrome-number/

TEST_CASES = [
        ({"x": 121}, True),
        ({"x": -121}, False),
        ({"x": 10}, False),
]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    for inputs,expected_output in TEST_CASES:
        actual_output = Solution().isPalindrome(**inputs)
        assert actual_output == expected_output, f"{inputs=}, {actual_output=}, {expected_output=}"

    print("all passed!")

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


if __name__ == "__main__":
    test_cases = [
            ({"s": "abcabcbb"}, 3),
    ]
    for inputs,expected_output in test_cases:
        actual_output = Solution().lengthOfLongestSubstring(**inputs)
        assert actual_output == expected_output, f"{inputs=}, {actual_output=}, {expected_output=}"

    print("all passed!")


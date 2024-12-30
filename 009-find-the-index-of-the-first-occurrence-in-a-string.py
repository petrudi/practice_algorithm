# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

TEST_CASES = [
        ({"haystack": "sadbutsad", "needle": "sad"}, 0),
        ({"haystack": "hello", "needle": "ll"}, 2),
]


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack)):
            if haystack[idx:idx+len(needle)] == needle:
                return idx
        return -1
        

if __name__ == "__main__":
    for inputs,expected_output in TEST_CASES:
        actual_output = Solution().strStr(**inputs)
        assert actual_output == expected_output, f"{inputs=}, {actual_output=}, {expected_output=}"

    print("all passed!")

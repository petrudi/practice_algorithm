# https://leetcode.com/problems/longest-common-prefix/

TEST_CASES = [
    ({"strs": ["flower","flow","flight"]}, "fl"),
    ({"strs": ["flower","flow","flight"]}, ""),
]


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if len(strs)==1:
            return prefix

        for s in strs[1:]:
            while (not s.startswith(prefix)):
                prefix = prefix[:-1]

        return prefix


if __name__ == "__main__":
    for inputs,expected_output in test_cases:
        actual_output = Solution().longestCommonPrefix(**inputs)
        assert actual_output == expected_output, f"{inputs=}, {actual_output=}, {expected_output=}"

    print("all passed!")

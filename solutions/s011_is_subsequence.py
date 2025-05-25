# https://leetcode.com/problems/is-subsequence/


TEST_CASES = [
    ({"s": "abc", "t": "ahbgdc"}, True),
    ({"s": "axc", "t": "ahbgdc"}, False),
]


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0
        p2 = 0

        while p2 < len(t) and p1 < len(s):
            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
                continue
            p2 += 1

        if p1 == len(s):
            return True

        return False


if __name__ == "__main__":
    for inputs, expected_output in TEST_CASES:
        actual_output = Solution().isSubsequence(**inputs)
        assert actual_output == expected_output, (
            f"{inputs=}, {actual_output=}, {expected_output=}"
        )

    print("all passed!")

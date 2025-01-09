# https://leetcode.com/problems/isomorphic-strings/
# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        p = 0
        ht1 = {}
        ht2 = {}

        if len(s) != len(t):
            return False

        while p < len(s):
            if ht1.get(s[p]) is not None:
                if ht1.get(s[p]) != t[p]:
                    return False
            elif ht2.get(t[p]) is not None:
                if ht2.get(t[p]) != s[p]:
                    return False

            ht1[s[p]] = t[p]
            ht2[t[p]] = s[p]
            p += 1

        return True

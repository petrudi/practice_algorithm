# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ht1 = {}
        ht2 = {}
        s = s.split()
        if len(pattern) != len(s):
            return False

        p = 0
        while p < len(pattern):
            if pattern[p] in ht1 and ht1[pattern[p]] != s[p]:
                return False
            ht1[pattern[p]] = s[p]
            if s[p] in ht2 and ht2[s[p]] != pattern[p]:
                return False
            ht2[s[p]] = pattern[p]
            p += 1
        return True

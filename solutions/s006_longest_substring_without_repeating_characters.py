# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        m = 0
        mem = set()
        while r < len(s):
            # validate and clean substring
            # calculate max
            # update set
            while s[r] in mem:
                mem.remove(s[l])
                l += 1
            w = r - l + 1
            m = max(m, w)
            mem.add(s[r])
            r += 1

        return m



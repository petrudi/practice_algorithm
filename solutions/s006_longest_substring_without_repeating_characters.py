# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        m = 0
        mem:dict[str,int] = {} #item,index
        while r < len(s):
            # validate and clean substring
            # calculate max
            # update set
            if s[r] in mem:
                l = mem[s[r]] + 1
            w = r - l + 1
            m = max(m, w)
            mem[s[r]] = r
            r += 1

        return m



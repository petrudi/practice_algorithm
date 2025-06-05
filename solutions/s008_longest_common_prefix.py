# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if len(strs) == 1:
            return prefix

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]

        return prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        first, others = strs[0], strs[1:]
        prefix = first
        for w in others:
            i = 0
            while i < len(prefix) and i < len(w) and prefix[i] == w[i]:
                i += 1

            prefix = prefix[:i]
        return prefix



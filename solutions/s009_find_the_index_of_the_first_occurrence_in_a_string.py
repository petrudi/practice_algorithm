"""
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle == "":
            return 0

        for idx in range(len(haystack)):
            if haystack[idx : idx + len(needle)] == needle:
                return idx
        return -1

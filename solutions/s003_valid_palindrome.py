# https://leetcode.com/problems/valid-palindrome/

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alphanumeric: str = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
        l = 0
        r = len(only_alphanumeric) - 1
        while l<r:
            if only_alphanumeric[l] != only_alphanumeric[r]:
                return False
            l += 1
            r -= 1

        return True



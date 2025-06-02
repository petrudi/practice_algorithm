# https://leetcode.com/problems/valid-palindrome/

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_alphanumeric: str = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
        p_start = 0
        p_end = len(only_alphanumeric) - 1
        for i in range(len(only_alphanumeric)):
            if only_alphanumeric[p_start] != only_alphanumeric[p_end]:
                return False
            p_start += 1
            p_end -= 1

            if p_start >= p_end:
                return True

        return True



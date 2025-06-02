# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        after_removing: str = self.__remove_non_alphanumeric_characters(s)
        p_start = 0
        p_end = len(after_removing) - 1
        for i in range(len(after_removing)):
            if after_removing[p_start] != after_removing[p_end]:
                return False
            p_start += 1
            p_end -= 1

            if p_start >= p_end:
                return True

        return True

    @staticmethod
    def __remove_non_alphanumeric_characters(s: str) -> str:
        import re

        return re.sub(r"[^a-zA-Z0-9]", "", s.lower())


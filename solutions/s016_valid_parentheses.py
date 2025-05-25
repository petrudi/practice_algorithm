# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        valid = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        if len(s) % 2 != 0:
            return False
        for chr in s:
            if chr in valid.keys():
                stk.append(chr)
                continue
            if not stk or stk and valid[stk.pop()] != chr:
                return False
        return len(stk) == 0

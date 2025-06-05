# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter: dict[str, int] = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        for c in t:
            if counter.get(c, 0) == 0:
                return False
            counter[c] -= 1

        return True

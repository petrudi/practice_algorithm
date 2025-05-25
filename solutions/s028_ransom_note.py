# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ht = Counter(magazine)

        for l in ransomNote:
            if l not in ht or ht[l] == 0:
                return False

            ht[l] -= 1

        return True

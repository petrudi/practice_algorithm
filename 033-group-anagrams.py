# https://leetcode.com/problems/group-anagrams/


from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for w in strs:
            c = ''.join(sorted(w))
            map[c].append(w)

        return list(map.values())

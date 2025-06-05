# https://leetcode.com/problems/number-of-different-integers-in-a-string/


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = "".join([w if w.isnumeric() else " " for w in word])
        word = word.split()
        word = set([int(w) for w in word])
        return len(word)


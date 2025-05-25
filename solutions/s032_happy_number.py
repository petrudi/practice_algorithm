class Solution:
    def isHappy(self, n: int) -> bool:
        ht = set()
        while n not in ht:
            sq = 0
            ht.add(n)
            while n != 0:
                d = n % 10
                n //= 10
                sq += d**2
            if sq == 1:
                return True

            n = sq
        return False

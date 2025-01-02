class Solution1: # time: O(n), space O(n)
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


class Solution2: # using stack, time: O(n), space O(n)
    def reverseWords(self, s: str) -> str:
        s = s.split()
        stk = []
        for w in s:
            stk.append(w)

        r = []
        while stk:
            r.append(stk.pop())
        return " ".join(r)


class Solution3: # two pointers, time: O(n), space O(n)
    def reverseWords(self, s: str) -> str:
        s = s.split()
        l ,r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
        
        return " ".join(s)

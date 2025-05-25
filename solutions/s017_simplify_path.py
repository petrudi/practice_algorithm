# https://leetcode.com/problems/simplify-path/


class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stk = []
        for idx, part in enumerate(parts):
            if stk and part == "..":
                stk.pop()
            elif part not in ("", ".", ".."):
                stk.append(part)
        return "/" + "/".join(stk)

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        m = 0
        mem = set()
        while r < len(s):
            # validate and clean substring
            # calculate max
            # update set
            while s[r] in mem:
                mem.remove(s[l])
                l += 1
            w = r - l + 1
            m = max(m, w)
            mem.add(s[r])
            r +=1

        return m


if __name__ == "__main__":
    test_cases = [
            ({"s": "abcabcbb"}, 3),
    ]
    for inputs,expected_output in test_cases:
        actual_output = Solution().lengthOfLongestSubstring(**inputs)
        assert actual_output == expected_output, f"{inputs=}, {actual_output=}, {expected_output=}"

    print("all passed!")


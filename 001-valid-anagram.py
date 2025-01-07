# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter: dict[str, int] = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        for c in t:
            if c not in counter or counter[c] == 0:
                return False
            counter[c] -= 1
        all_zero = all(x == 0 for x in counter.values())
        if all_zero:
            return True
        return False

if __name__ == "__main__":
    test_cases = [
        ({"s": "anagram","t": "nagaram"}, True),
        ({"s": "rat","t": "car"}, True),
    ]
    for inputs,expected_output in test_cases:
        actual_output = Solution().isAnagram(**inputs)
        assert actual_output == expected_output

    print("all passed!")

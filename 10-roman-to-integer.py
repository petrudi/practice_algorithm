# https://leetcode.com/problems/roman-to-integer/s

TEST_CASES = [
        ({"s": "III"}, 3),
        ({"s": "LVIII"}, 58),
]


class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        number = 0
        idx = 0
        while idx < len(s):
            current = s[idx]
            if idx + 1 < len(s) and (current_with_next := current + s[idx+1]) in table:
                number += table[current_with_next]
                idx+=2
                continue

            number += table[current]
            idx+=1
            continue

        return number


if __name__ == "__main__":
    for inputs,expected_output in TEST_CASES:
        actual_output = Solution().romanToInt(**inputs)
        assert actual_output == expected_output, f"{inputs=}, {actual_output=}, {expected_output=}"

    print("all passed!")

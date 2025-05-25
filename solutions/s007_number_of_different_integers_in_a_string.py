# https://leetcode.com/problems/number-of-different-integers-in-a-string/


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = "".join([w if w.isnumeric() else " " for w in word])
        word = word.split()
        word = set([int(w) for w in word])
        return len(word)


if __name__ == "__main__":
    test_cases = [
        ({"word": "a123bc34d8ef34"}, 3),
        ({"word": "leet1234code234"}, 2),
        ({"word": "a1b01c001"}, 1),
    ]
    for inputs, expected_output in test_cases:
        actual_output = Solution().numDifferentIntegers(**inputs)
        assert actual_output == expected_output, (
            f"{inputs=}, {actual_output=}, {expected_output=}"
        )

    print("all passed!")

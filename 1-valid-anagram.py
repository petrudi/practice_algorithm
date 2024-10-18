# https://leetcode.com/problems/valid-anagram/


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        number_of_visited_letters: dict[str, int] = {}
        for c in s:
            if c in number_of_visited_letters:
                number_of_visited_letters[c] += 1
                continue
            number_of_visited_letters[c] = 1
        print(number_of_visited_letters)
        for c in t:
            if c not in number_of_visited_letters:
                return False
            if number_of_visited_letters[c] == 0:
                return False
            number_of_visited_letters[c] -= 1
        print(number_of_visited_letters)
        all_zero = all(x == 0 for x in number_of_visited_letters.values())
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

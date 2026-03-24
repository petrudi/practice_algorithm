import pytest
from ..solutions.s033_group_anagrams import Solution


def normalize(groups):
    return sorted([sorted(g) for g in groups])


TEST_CASES = [
    (
        {"strs": ["eat", "tea", "tan", "ate", "nat", "bat"]},
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    ({"strs": [""]}, [[""]]),
    ({"strs": ["a"]}, [["a"]]),
    # Edge cases
    ({"strs": []}, []),
    ({"strs": ["ab", "ba", "abc", "cab", "bca", "x"]}, [["ab", "ba"], ["abc", "bca", "cab"], ["x"]]),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_groupAnagrams(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.groupAnagrams(**inputs_dict)
    assert normalize(actual_output) == normalize(expected_output), (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


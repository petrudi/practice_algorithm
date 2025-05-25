import pytest
from ..solutions.s002_summary_ranges import Solution

TEST_CASES = [
    ({"nums": [0, 1, 2, 4, 5, 7]}, ["0->2", "4->5", "7"]),
    ({"nums": [0, 2, 3, 4, 6, 8, 9]}, ["0", "2->4", "6", "8->9"]),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_summaryRanges(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.summaryRanges(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )

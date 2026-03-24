import pytest
from ..solutions.s017_simplify_path import Solution


TEST_CASES = [
    ({"path": "/home/"}, "/home"),
    ({"path": "/home//foo/"}, "/home/foo"),
    ({"path": "/home/user/Documents/../Pictures"}, "/home/user/Pictures"),
    ({"path": "/../"}, "/"),
    ({"path": "/.../a/../b/c/../d/./"}, "/.../b/d"),
    # Edge cases
    ({"path": "/"}, "/"),
    ({"path": "/./././"}, "/"),
    ({"path": "/a/./b/../../c/"}, "/c"),
    ({"path": "/a//b////c/d//././/.."}, "/a/b/c"),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_simplifyPath(inputs_dict, expected_output):
    solver = Solution()
    actual_output = solver.simplifyPath(**inputs_dict)
    assert actual_output == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {actual_output}"
    )


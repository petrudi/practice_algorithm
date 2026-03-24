import pytest
from ..solutions.s024_min_stack import MinStack


TEST_CASES = [
    (
        {
            "ops": [
                ("push", -2),
                ("push", 0),
                ("push", -3),
                ("getMin", None),
                ("pop", None),
                ("top", None),
                ("getMin", None),
            ]
        },
        [-3, None, 0, -2],
    ),
    (
        {
            "ops": [
                ("push", 5),
                ("getMin", None),
                ("push", 3),
                ("getMin", None),
                ("push", 7),
                ("getMin", None),
                ("pop", None),
                ("getMin", None),
            ]
        },
        [5, 3, 3, None, 3],
    ),
]


@pytest.mark.parametrize("inputs_dict, expected_output", TEST_CASES)
def test_MinStack(inputs_dict, expected_output):
    stk = MinStack()
    outputs = []
    for op, arg in inputs_dict["ops"]:
        if op == "push":
            stk.push(arg)
        elif op == "pop":
            stk.pop()
            outputs.append(None)
        elif op == "top":
            outputs.append(stk.top())
        elif op == "getMin":
            outputs.append(stk.getMin())
        else:
            raise ValueError(f"Unknown operation: {op}")

    assert outputs == expected_output, (
        f"Failed for input {inputs_dict}. Expected {expected_output}, got {outputs}"
    )


def test_MinStack_top_empty_raises():
    stk = MinStack()
    with pytest.raises(IndexError):
        stk.top()


def test_MinStack_getMin_empty_raises():
    stk = MinStack()
    with pytest.raises(IndexError):
        stk.getMin()


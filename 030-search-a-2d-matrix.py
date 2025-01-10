from typing import List


TEST_CASES = [
        ({"matrix": [[1,3,5,7],[10,11,16,20],[23,30,34,50]], "target": 11}, True),
        ({"matrix": [[1,3]], "target": 3}, True),
]



def binary_search(numbers:List[int], target: int):
    left = 0
    right = len(numbers) - 1
    was_found = False
    while (left<=right):
        mid = (left + right) // 2
        print(f"{left=} {mid=} {right=}")
        if target < numbers[mid]:
            right = mid - 1
        elif target > numbers[mid]:
            left = mid
        else:
            was_found = True
            return mid, was_found

        if left == mid:
            return mid, was_found

        if right-mid<=1:
            return mid, was_found
    return mid, was_found


def binary_search2(numbers:List[int], target: int):
    left = 0
    right = len(numbers) - 1
    was_found = False
    while (left<=right):
        mid = (left + right) // 2
        print(f"{left=} {mid=} {right=}")
        if target < numbers[mid]:
            right = mid - 1
        elif target > numbers[mid]:
            left = mid + 1
        else:
            was_found = True
            return mid, was_found

        if left == mid:
            return mid, was_found

    if right-mid<=1:
        return mid, was_found
    return mid, was_found

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1:
            if len(matrix[0]) == 1:
                return target in matrix[0]

        a = [row[0] for row in matrix]
        idx , was_found = binary_search(a, target)
        if was_found:
            return True

        
        idx , was_found = binary_search2(matrix[idx], target)
        return was_found

if __name__ == "__main__":
    for inputs,expected_output in TEST_CASES:
        actual_output = Solution().searchMatrix(**inputs)
        assert actual_output == expected_output, f"{inputs=}, {actual_output=}, {expected_output=}"

    print("all passed!")

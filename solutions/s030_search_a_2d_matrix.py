# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2
            r = mid // n
            c = mid % n
            v = matrix[r][c]
            if v == target:
                return True
            if v < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

def binary_search(numbers:List[int], target: int):
    left = 0
    right = len(numbers) - 1
    was_found = False
    while (left<=right):
        mid = (left + right) // 2
        if target < numbers[mid]:
            right = mid - 1
        elif target > numbers[mid]:
            left = mid + 1
        else:
            was_found = True
            return mid, was_found

    if left == mid:
        return mid-1, was_found
    print(f"{left=} {mid=}")
    return mid, was_found
    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return target in matrix[0]

        a = [row[0] for row in matrix]
        idx , was_found = binary_search(a, target)
        print(f"{idx=} {was_found=}")
        if was_found:
            return True

        
        idx , was_found = binary_search(matrix[idx], target)
        return was_found

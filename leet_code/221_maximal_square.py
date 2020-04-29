"""
221. Maximal Square
https://leetcode.com/problems/maximal-square/

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

from typing import List
from collections import deque
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        matrix = [[int(matrix[i][j]) for j in range(len(matrix[i]))] for i in range(len(matrix))]

        max_width = 0
        for row in matrix:
            if 1 in row:
                max_width = 1

        if max_width == 0:
            return 0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1

                if matrix[i][j] > max_width:
                    max_width = matrix[i][j]

        # print(max_width ** 2)
        return max_width ** 2


matrix = [
    ['1', '0', '1', '0', '0', '0'],
    ['1', '0', '1', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '0'],
    ['1', '1', '1', '1', '1', '1'],
    ['1', '1', '0', '1', '0', '0']
]
print(Solution().maximalSquare(matrix) == 9)

matrix = [
    ['1', '0'],
    ['0', '0'],
]
print(Solution().maximalSquare(matrix) == 1)

matrix = [
    ['1', '1'],
    ['1', '1'],
]
print(Solution().maximalSquare(matrix) == 4)

print(Solution().maximalSquare(matrix = [['1']]) == 1)
print(Solution().maximalSquare(matrix = [['0']]) == 0)

matrix = [
    ["0","1","1","0","1"],
    ["1","1","0","1","0"],
    ["0","1","1","1","0"],
    ["1","1","1","1","0"],
    ["1","1","1","1","1"],
    ["0","0","0","0","0"]
]
print(Solution().maximalSquare(matrix) == 9)

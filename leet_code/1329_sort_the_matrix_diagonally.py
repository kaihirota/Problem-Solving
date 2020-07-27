"""
1329. Sort the Matrix Diagonally
https://leetcode.com/problems/sort-the-matrix-diagonally/

Given a m * n matrix mat of integers, sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

Example 1:
Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]


Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""
from typing import List
from collections import defaultdict

class Solution:

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        n, m = len(mat), len(mat[0])
        diagonals = defaultdict(list)

        for i in range(n):
            for j in range(m):
                print(i, j, i-j)
                diagonals[i - j] += mat[i][j],

        for k in diagonals:
            diagonals[k].sort(reverse=1)

        for key in sorted(diagonals.keys()):
            print(key, diagonals[key])

        for i in range(n):
            for j in range(m):
                mat[i][j] = diagonals[i - j].pop()

        return mat

mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Solution().diagonalSort(mat = mat) == [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

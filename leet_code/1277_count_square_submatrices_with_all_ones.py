"""
1277. Count Square Submatrices with All Ones
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation:
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation:
There are 6 squares of side 1.
There is 1 square of side 2.
Total number of squares = 6 + 1 = 7.

Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""
from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        explanation

        If A[i][j] == 0, no possible square.
        If A[i][j] == 1,
        we compare the size of square dp[i-1][j-1], dp[i-1][j] and dp[i][j-1].
        min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 is the maximum size of square that we can find
        """
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])

        return sum(map(sum, matrix))

matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
assert Solution().countSquares(matrix) == 15

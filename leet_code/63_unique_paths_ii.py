"""
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * m for i in range(n)]

        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        if i == 0 and j == 0:
                            dp[i][j] = 1
                        elif i == 0 and j > 0 and obstacleGrid[i][j-1] != 1:
                            dp[i][j] = dp[i][j-1]
                        elif j == 0 and i > 0 and obstacleGrid[i-1][j] != 1:
                            dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1] + dp[i-1][j]

        # for row in dp:
        #     print(row)
        return dp[-1][-1]


obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
assert Solution().uniquePathsWithObstacles(obstacleGrid) == 2
assert Solution().uniquePathsWithObstacles([[1,0]]) == 0
assert Solution().uniquePathsWithObstacles([[0]]) == 1
obstacleGrid = [
    [0,1,0,0,0],
    [1,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
assert Solution().uniquePathsWithObstacles(obstacleGrid) == 0

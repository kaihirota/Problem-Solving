"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m for i in range(n)]

        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

        return dp[-1][-1]


assert Solution().uniquePaths(m=3, n=2) == 3
assert Solution().uniquePaths(m=7, n=3) == 28

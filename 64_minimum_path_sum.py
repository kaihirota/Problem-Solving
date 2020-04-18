"""
64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
# # solution 1: time limit exceeded
# class Solution:
#     # def minPathSum(self, grid: List[List[int]]) -> int:
#     def minPathSum(self, grid):
#         x, y = len(grid)-1, len(grid[0])-1
#
#         def DFS(grid, i, j):
#             if i < 0 or j < 0:
#                 return float("inf")
#             if i == 0 and j == 0:
#                 return grid[0][0]
#
#             return grid[i][j] + min(DFS(grid, i-1, j), DFS(grid, i, j-1))
#
#         return DFS(grid, x, y)

# solution 2: passed
class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif i > 0 and j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]

# Andrew's solution
class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        path = []

        for idx1, row in enumerate(grid):
            for idx2, num in enumerate(row):

                if path == []:
                    path.append(num)

                elif len(path) < len(grid[0]):
                    path.append(path[-1] + num)

                elif idx2 == 0:
                    path[idx2] += num

                else:
                    path[idx2] = min(path[idx2], path[idx2-1]) + num

        return path[-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
x = Solution().minPathSum(grid)
print(x)

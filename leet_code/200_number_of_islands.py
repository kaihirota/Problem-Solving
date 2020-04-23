"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
def BFS(grid, x, y):
    stack = [(x, y)]

    while stack:
        i, j = stack.pop()

        if grid[i][j] == '1':
            grid[i][j] = '0'

            if i + j == 0:
                # upper left corner
                if len(grid) > 1:
                    stack.append((i+1, j))
                if len(grid[0]) > 1:
                    stack.append((i, j+1))
            elif i + j == len(grid) + len(grid[0]) - 2:
                # bottom right corner
                stack.append((i-1, j))
                stack.append((i, j-1))
            elif i == 0 and j == len(grid[0]) - 1:
                # upper right corner
                stack.append((i, j-1))
                stack.append((i+1, j))
            elif i == len(grid) - 1 and j == 0:
                # bottom left corner
                stack.append((i-1, j))
                stack.append((i, j+1))
            elif i == 0 or i == len(grid) - 1:
                # top or bottom row
                stack.append((i, j-1))
                stack.append((i, j+1))
                if len(grid) > 1:
                    if i == 0:
                        stack.append((i+1, j))
                    else:
                        stack.append((i-1, j))
            elif j == 0 or j == len(grid[0]) - 1:
                # right or left column
                stack.append((i-1, j))
                stack.append((i+1, j))
                if len(grid[0]) > 1:
                    if j == 0:
                        stack.append((i, j+1))
                    else:
                        stack.append((i, j-1))
            elif len(grid) + len(grid[0]) >= 6:
                stack.append((i-1, j))
                stack.append((i+1, j))
                stack.append((i, j-1))
                stack.append((i, j+1))

    return grid


class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    def numIslands(self, grid):
        counter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    grid = BFS(grid, i, j)
                    counter += 1

        return counter


class Solution:
    # solution from leetcode
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count


    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

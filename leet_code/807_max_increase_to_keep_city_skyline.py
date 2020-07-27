"""
807. Max Increase to Keep City Skyline
https://leetcode.com/problems/max-increase-to-keep-city-skyline/

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation:
The grid is:
[ [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]
"""
from typing import List
from collections import defaultdict

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        xy_limit = {
            'i': defaultdict(int),
            'j': defaultdict(int)
        }
        total_increase = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                xy_limit['i'][i] = max(xy_limit['i'][i], grid[i][j])
                xy_limit['j'][j] = max(xy_limit['j'][j], grid[i][j])

        for i in range(len(grid)):
            horizontal_max = xy_limit['i'][i]
            for j in range(len(grid[0])):
                vertical_max = xy_limit['j'][j]

                if grid[i][j] != horizontal_max and grid[i][j] != vertical_max:
                    total_increase += min(horizontal_max, vertical_max) - grid[i][j]
                    grid[i][j] = min(horizontal_max, vertical_max)

        return total_increase


grid = [
    [3,0,8,4],
    [2,4,5,7],
    [9,2,6,3],
    [0,3,1,0]
]
assert Solution().maxIncreaseKeepingSkyline(grid) == 35

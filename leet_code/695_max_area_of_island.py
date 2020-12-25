"""
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/
"""
from typing import List
from collections import defaultdict
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.board_map = defaultdict(int)
        adj = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.board_map[(i, j)] = grid[i][j]

        def DFS(pos, area=0):
            x, y = pos
            grid[x][y] = 0
            self.board_map[(x, y)] = 0
            area += 1

            for dx, dy in adj:
                if self.board_map[(x+dx, y+dy)] == 1:
                    area = DFS((x+dx, y+dy), area)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, DFS((i, j)))

        return max_area


Solution().maxAreaOfIsland([
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
])
Solution().maxAreaOfIsland([[0,0,0,0,0,0,0,0]])

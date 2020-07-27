"""
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
"""
from collections import defaultdict
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        data = defaultdict(int)

        for i in range(rows):
            for j in range(cols):
                data[(i, j)] = grid[i][j]

        rotten = [[(i, j) for (i, j), val in data.items() if val == 2]]
        n_fresh = len([(i, j) for (i, j), val in data.items() if val == 1])

        minutes = 0

        while n_fresh > 0:

            if len(rotten) == 0 or len(rotten[0]) == 0:
                return -1

            rotten_oranges = rotten.pop()
            next_gen = []

            for i, j in rotten_oranges:
                for adj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if data[adj] == 1:
                        data[adj] = 2
                        n_fresh -= 1
                        next_gen += adj,

            if len(next_gen) > 0:
                rotten += next_gen,
                minutes += 1

        return minutes


assert Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert Solution().orangesRotting([[0,2]]) == 0
assert Solution().orangesRotting([[1],[1],[1],[1]]) == -1
assert Solution().orangesRotting([[2],[2],[1],[0],[1],[1]]) == -1

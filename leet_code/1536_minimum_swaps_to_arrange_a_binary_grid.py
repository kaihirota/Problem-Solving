"""
1536. Minimum Swaps to Arrange a Binary Grid
https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
"""
from typing import *

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        def count_trailing_zero(arr):
            idx = len(arr) - 1
            while idx >= 0 and arr[idx] == 0:
                idx -= 1
            return len(arr) - 1 - idx

        ranks = [count_trailing_zero(grid[i]) for i in range(len(grid))]

        # print('before: ', ranks)
        swaps = 0
        for i in range(len(ranks)):
            j = i
            while j < len(ranks) and ranks[j] < len(ranks) - 1 - i:
                j += 1

            if j == len(ranks):
                return -1

            tmp = ranks.pop(j)
            ranks.insert(i, tmp)
            swaps += j - i

        # print('after: ', ranks)
        # print(swaps)
        return swaps


assert Solution().minSwaps(grid = [[0,0,1],[1,1,0],[1,0,0]]) == 3
assert Solution().minSwaps(grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]) == -1
assert Solution().minSwaps(grid = [[1,0,0],[1,1,0],[1,1,1]]) == 0
assert Solution().minSwaps(grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]) == 2
assert Solution().minSwaps(grid = [[0,0],[0,1]]) == 0
assert Solution().minSwaps(grid = [[0,1,1,0],[1,1,1,0],[1,1,1,0],[1,0,0,0]]) == -1
assert Solution().minSwaps(grid = [[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]) == 2
assert Solution().minSwaps(grid = [[1,0,0,0],[1,0,0,0],[1,1,0,0],[0,1,0,0]]) == 0
Solution().minSwaps(grid = [[1,0,1,1,0,0,0,0,0,0,0],[1,1,1,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,0,0,0,0,0],[1,0,1,1,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0],[1,1,1,0,1,0,0,0,0,0,0]])

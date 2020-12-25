from typing import *

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        arr = [] # (zeros, i)
        for i in range(len(grid)):
            j = len(grid[0]) - 1
            zeros = 0
            while j >= 0 and grid[i][j] == 0:
                zeros += 1
                j -= 1
            arr += (zeros, i),

        for i, row in enumerate(sorted(arr, key=lambda x: x[0], reverse=True)):
            if row[0] < len(arr) - 1 - i:
                return -1
        # minimum_zero = sum([i for i in range(len(grid))])
        # total_zeros = sum([arr[i][0] for i in range(len(arr))])
        # if total_zeros < minimum_zero:
        #     return -1
        # found = False
        # for i in range(len(arr)):
        #     if arr[i][0] >= len(arr) - 1:
        #         found = True
        # if found is False:
        #     return -1
        # check = sorted([arr[i][0] for i in range(len(arr))])
        # if check != list(range(len(grid))):
        #     return -1

        swaps = 0
        sorted_arr = sorted(arr, key=lambda x: x[0], reverse=True)
        i = 0
        while arr != sorted_arr:
            if arr[i][0] < arr[i+1][0]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps += 1
            if i == len(arr) - 2:
                i = 0
            else:
                i += 1
        return swaps

assert Solution().minSwaps(grid = [[0,0,1],[1,1,0],[1,0,0]]) == 3
assert Solution().minSwaps(grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]) == -1
assert Solution().minSwaps(grid = [[1,0,0],[1,1,0],[1,1,1]]) == 0
assert Solution().minSwaps(grid = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]) == 2
assert Solution().minSwaps(grid = [[0,0],[0,1]]) == 0
assert Solution().minSwaps(grid = [[0,1,1,0],[1,1,1,0],[1,1,1,0],[1,0,0,0]]) == -1

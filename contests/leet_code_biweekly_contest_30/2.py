from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        dp = [[0] * (n + 1) for i in range(n + 1)]
        dp[0][1] = nums[0]

        for i in range(n):
            for j in range(i+1, n+1):
                dp[i][j] = dp[i][j-1] + nums[j-1]

        rangeSums = sorted([item for row in dp for item in row if item != 0])
        return sum(rangeSums[left-1:right])



Solution().rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5)

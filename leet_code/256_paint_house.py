"""
256. Paint House
https://leetcode.com/problems/paint-house/
"""
from typing import List
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) > 0:
            dp = [[float('inf')] * len(costs[0]) for i in range(len(costs))]
            dp[0] = costs[0]
            for i in range(1, len(costs)):
                for j in range(len(costs[0])):
                    for g in range(len(costs[0])):
                        if g != j:
                            dp[i][j] = min(dp[i][j], costs[i][j] + dp[i-1][g])


            return min(dp[-1])
        else:
            return 0

assert Solution().minCost([[17,2,17],[16,16,5],[14,3,19]]) == 10

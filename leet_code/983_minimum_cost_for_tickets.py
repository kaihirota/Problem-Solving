"""
983. Minimum Cost For Tickets
https://leetcode.com/problems/minimum-cost-for-tickets/
"""
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        days = set(days)
        last_day = max(days)

        for i in range(1, 366):
            if i in days:
                dp[i] = min(
                    dp[i - 1] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2]
                )
            else:
                dp[i] = dp[i-1]

        return dp[-1]


assert Solution().mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]) == 11
assert Solution().mincostTickets(days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]) == 17

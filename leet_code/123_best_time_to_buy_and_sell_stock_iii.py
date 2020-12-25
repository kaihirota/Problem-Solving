"""
123. Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        pref = [0] * len(prices)
        curr_min = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            curr_min = min(curr_min, prices[i])
            max_profit = max(max_profit, prices[i] - curr_min)
            pref[i] = max_profit

        suf = [0] * len(prices)
        curr_max = 0
        max_profit = 0
        for i in range(len(prices)-1, -1, -1):
            suf[i] = max_profit
            curr_max = max(curr_max, prices[i])
            max_profit = max(max_profit, curr_max - prices[i])

        print(pref)
        print(suf)
        return max([p + s for p, s in zip(pref, suf)])


assert Solution().maxProfit([3,3,5,0,0,3,1,4]) == 6
assert Solution().maxProfit([1,2,3,4,5]) == 4
assert Solution().maxProfit([7,6,4,3,1]) == 0

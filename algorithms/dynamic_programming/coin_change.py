class Solution(object):
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[-1] == float('inf'):
            return -1

        print(dp)
        return dp[-1]


coins = [1, 2, 5]
amount = 11
assert Solution().coinChange(coins, amount) == 3

def knapsack(values, weights, lim):
    dp = [-1] * (lim + 1)
    dp[0] = 0
    global_max = 0

    for i in range(1, lim + 1):
        local_max = 0
        for j in range(len(values)):
            if weights[j] <= i:
                local_max = max(local_max, values[j] + dp[i - weights[j]])
        dp[i] = local_max
        global_max = max(global_max, local_max)

    return global_max


def knapsack(values, weights, lim):
    dp = [[0] * (lim + 1) for i in range(len(values) + 1)]

    for i in range(1, len(values) + 1):
        for j in range(1, lim + 1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], values[i-1] + dp[i-1][j-weights[i-1]])
    return dp[-1][-1]

v = [1, 6, 18, 22, 28]
w = [1, 2, 5, 6, 7]
W = 11
assert knapsack(v, w, W) == 40

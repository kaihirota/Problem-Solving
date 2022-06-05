"""
There are N houses for sale.
The i-th house costs Ai dollars to buy.
You have a budget of B dollars to spend.

What is the maximum number of houses you can buy?

input:
3
4 100
20 90 40 90  Case #1: 2
4 50
30 30 10 10  Case #2: 3
3 300
999 999 999  Case #3: 0
"""
test = int(input())
for t in range(1, test+1):
    n, budget = list(map(int, input().strip().split()))
    cost = sorted(list(map(int, input().strip().split())))

    curr_cost = 0
    houses = 0
    for i in range(len(cost)):
        if cost[i] <= budget:
            budget -= cost[i]
            houses += 1
        else:
            break

    print("Case #" + str(t) + ": " + str(houses))

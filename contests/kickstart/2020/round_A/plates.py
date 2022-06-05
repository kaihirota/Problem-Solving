test = int(input())
for t in range(1, test+1):
    n, k, p = list(map(int, input().strip().split()))

    rows = []
    for i in range(n):
        rows.append(list(map(int, input().strip().split())))

    dp = [[0 for i in range(k)] for j in range(n)]
    for i in range(n):
        for j in range(1, k):
            rows[i][j] = rows[i][j-1]

    maxp = 0
    for i in range(n):
        for j in range(k):
            maxp = rows[i][j]

    for row in dp:
        print(row)

    # print("Case #" + str(t) + ": " + str(rows))

# # solution
# T = int (input())
# for t in range(1, T+1):
# 	n, k, p = [int(_) for _ in input().split()]
# 	stacks = [[] for _ in range(n)]
# 	for i in range(n):
# 		stacks[i] = [int(_) for _ in input().split()]
#
# 	res = 0
# 	dp = [0]*(p+1)
# 	for i in range(n):
# 		dpnext = [_ for _ in dp]
# 		for j in range(p+1):
# 			run = 0
# 			for m in range(min(k, p-j)):
# 				run += stacks[i][m]
# 				dpnext[j] = max(dpnext[j], dp[j+m+1] + run)
# 		dp = dpnext
# 	print ("Case #{}: {}".format(t, max(dp)))

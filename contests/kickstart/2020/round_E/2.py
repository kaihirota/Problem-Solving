test = int(input())
for t in range(1, test+1):
    n, a, b, c = list(map(int, input().strip().split()))

    left = list(range(n-a+1, n+1)) + ([0] * (n - a))
    right = ([0] * (n - b)) + list(range(n, n-b, -1))

    print(left)
    print(right)
    # print("Case #" + str(t) + ": " + str(broken_rules))

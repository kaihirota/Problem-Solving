T = int(input())
for t in range(T):
    target, a, b, c, d = map(int, input().strip().split())
    """
    x2 cost a
    x3 cost b
    x5 cost c
    +- 1 cost d
    """
    num = 0
    cost = 0
    while num < target:
        v1 = num * 2, cost + a
        v2 = num * 3, cost + b
        v3 = num * 5, cost + c
        if abs(num + 1 - target) < abs(num - 1 - target):
            v4 = num + 1, cost + d
        else:
            v4 = num - 1, cost + d

        print(v1, v2, v3, v4)

        num, cost = min([v1, v2, v3, v4], key=lambda x: target - x[0] if 0 < x[0] <= target else float('inf'))
        print(num, cost)
        # break

    print(num, cost)

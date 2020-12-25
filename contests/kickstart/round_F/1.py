from collections import deque

test = int(input())
for t in range(1, test+1):
    n, lim = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    arr = deque([(i, item) for i, item in enumerate(arr, 1)])
    left = []

    while arr:
        idx, amount = arr.popleft()
        if amount <= lim:
            left.append(str(idx))
        else:
            arr.append((idx, amount - lim))

    print("Case #" + str(t) + ": " + " ".join(left))

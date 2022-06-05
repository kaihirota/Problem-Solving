test = int(input())
for t in range(1, test+1):
    n, c = list(map(int, input().strip().split()))
    left = []
    right = []
    for i in range(n):
        l, r = list(map(int, input().strip().split()))
        left += l,
        right += r,

    arr = [0] * max(right)
    for l, r in zip(left, right):
        for i in range(l+1, r):
            arr[i] += 1
    
    intervals = [item for item in zip(left, right)]
    intervals = sorted(intervals)
    print(intervals)

    vals = sorted([(idx, count) for idx, count in enumerate(arr)], key=lambda x: x[1], reverse=True)
    i = 0
    ret = len(left)
    while i < c and i < len(vals):
        idx, count = vals[i]
        if count == 0:
            break
        else:
            ret += count
        i += 1
    
    print("Case #" + str(t) + ": " + str(ret))

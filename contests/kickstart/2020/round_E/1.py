test = int(input())
for t in range(1, test+1):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    diff = [0] * n

    for i in range(n-1):
        diff[i] = arr[i] - arr[i+1]

    max_length = 1
    curr_length = 1
    # print(diff)
    for i in range(1, n-1):
        if diff[i] == diff[i-1]:
            curr_length += 1
            max_length = max(max_length, curr_length + 1)
        else:
            curr_length = 1
    max_length = max(max_length, curr_length + 1)

    print("Case #" + str(t) + ": " + str(max_length))

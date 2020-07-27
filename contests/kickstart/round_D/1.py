test = int(input())
for t in range(1, test+1):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    days = 0
    curr_max = arr[0]

    if len(arr) == 1:
        days += 1
    else:
        for i in range(n):
            if i == 0:
                if arr[i] > arr[i+1]:
                    days += 1
            elif arr[i] > curr_max and ((i == (n - 1) or arr[i] > arr[i+1])):
                days += 1
            curr_max = max(curr_max, arr[i])

    print("Case #" + str(t) + ": " + str(days))

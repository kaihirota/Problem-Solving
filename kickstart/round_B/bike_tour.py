test = int(input())
for t in range(1, test+1):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    peaks = 0

    for i in range(len(arr)):
        if i == 0 or i == len(arr) - 1:
            continue
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            peaks += 1

    print("Case #" + str(t) + ": " + str(peaks))

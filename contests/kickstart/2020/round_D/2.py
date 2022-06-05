test = int(input())
for t in range(1, test+1):
    n = int(input())
    arr = list(map(int, input().strip().split()))

    broken_rules = 0
    curr_note = 1
    for i in range(len(arr)):
        if arr[i] > arr[i-1]:
            curr_note += 1
        elif arr[i] < arr[i-1]:
            curr_note -= 1
        if curr_note == 0:
            curr_note = 4
            broken_rules += 1
        elif curr_note == 5:
            curr_note = 0
            broken_rules += 1


    print("Case #" + str(t) + ": " + str(broken_rules))

test = int(input())
for t in range(1, test+1):
    n, k = list(map(int, input().strip().split()))
    arr = list(map(int, input().strip().split()))
    found = 0
    countdown = k

    for i in range(n):
        if arr[i] == countdown:
            countdown -= 1
            if countdown == 0:
                countdown = k
                found += 1
        else:
            countdown = k
            if arr[i] == countdown:
                countdown -= 1

    print("Case #" + str(t) + ": " + str(found))

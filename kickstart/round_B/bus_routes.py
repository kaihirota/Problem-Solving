test = int(input())
for t in range(1, test+1):
    n, d = list(map(int, input().strip().split()))
    x = list(map(int, input().strip().split()))
    depart_day = d

    for i in range(len(x)-1, -1, -1):
        if depart_day % x[i] == 0:
            continue
        elif depart_day // x[i] > 0:
            depart_day = x[i] * (depart_day // x[i])

    print("Case #" + str(t) + ": " + str(depart_day))

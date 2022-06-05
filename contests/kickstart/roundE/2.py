test = int(input())
for t in range(1, test+1):
    r, c, k = map(int, input().strip().split())
    r1, c1, r2, c2 = map(int, input().strip().split())

    cake = [[0] * c for _ in range(r)]
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            cake[i-1][j-1] = 1

    for row in cake:
        print(row)

    vertical = min(r1 - 1, r - r2)
    horizontal = min(c1 - 1, c - c2)

    w, h = r2 - r1 + 1, c2 - c1 + 1

    if not (vertical == 0 and horizontal == 0):
        # delicious part needs to be extracted
        # first cut into the cake
        vcuts, vremainder = divmod(vertical + h, k)
        hcuts, hremainder = divmod(horizontal + w, k)



    print(vertical, horizontal)

    # print("Case #" + str(t) + ": " + str(broken_rules))

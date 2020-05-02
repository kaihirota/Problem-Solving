test = int(input())
for t in range(1, test+1):

    s = list(map(int, list(input().strip())))
    # s = list(map(int, list("001124134")))
    # "00(11(2((4)))1((3(4))))"
    
    balanced = []
    open_par = 0
    for d in s:
        if d > open_par:
            diff = d - open_par
            balanced.append("(" * diff)
            open_par += diff
        elif d < open_par:
            diff = open_par - d
            balanced.append(")" * diff)
            open_par -= diff
        balanced.append(str(d))

    if open_par > 0:
        balanced.append(")" * open_par)

    # print("".join(balanced))
    print("Case #" + str(t) + ": " + "".join(balanced))

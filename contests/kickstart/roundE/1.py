
from itertools import permutations
test = int(input())
for t in range(1, test+1):
    s = tuple(list(input().strip()))
    found = False
    for pattern in permutations(s):
        idx = 0
        while idx < len(s) and s[idx] != pattern[idx]:
            idx += 1

        if idx == len(s):
            print("Case #" + str(t) + ": " + "".join(pattern))
            found = True
            break

    if not found:
        print("Case #" + str(t) + ": " + "IMPOSSIBLE")

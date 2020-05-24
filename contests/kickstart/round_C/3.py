# solution: https://codingcompetitions.withgoogle.com/kickstart/submissions/000000000019ff43/ZXhvamkyZQ
"""
input:
3
3
2 2 6
5
30 30 9 1 30
4
4 0 0 16

output:
Case #1: 1
Case #2: 3
Case #3: 9
"""
from collections import Counter

def nl():
    return [int(_) for _ in input().split()]

test = int(input())
for t in range(1, test+1):
    n = int(input())
    # arr = list(map(int, input().strip().split()))
    arr = nl()

    C = Counter()
    C[0] = 1
    ans = 0
    pref = 0

    for i, a in enumerate(arr):
        pref += a
        for i in range(int(((i+1)*100)**.5) + 2):
            ans += C[pref - i**2]
        C[pref] += 1

    print("Case #" + str(t) + ": " + str(ans))

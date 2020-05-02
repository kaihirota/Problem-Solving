import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

############################################################

def main():
    for q in range(II()):
        n, d = MI()
        xx = LI()
        for x in xx[::-1]:
            d = d // x * x
        print("Case #{}: {}".format(q + 1, d))

main()

############################################################

def main():
    for q in range(II()):
        n = II()
        hh = LI()
        ans = 0
        for i in range(1, n - 1):
            if hh[i - 1] < hh[i] > hh[i + 1]:
                ans += 1
        print("Case #{}: {}".format(q + 1, ans))

main()

############################################################

from collections import defaultdict

def main():
    def cnt(t):
        res = defaultdict(int)
        coe = 1
        cc = []
        for c in t:
            if c == "(":
                continue
            elif c.isdigit():
                coe *= int(c)
                cc.append(int(c))
            elif c == ")":
                coe //= cc.pop()
            else:
                res[c] += coe
        return res

    for q in range(II()):
        t = SI()
        md = 10**9
        ret = cnt(t)
        x = (ret["E"] - ret["W"]) % md
        y = (ret["S"] - ret["N"]) % md
        print("Case #{}: {} {}".format(q + 1, x + 1, y + 1))

main()

############################################################

# TLE
from collections import defaultdict

def main():
    memo = {}

    def P(x, y):
        if x * y == 0 or x >= w or y >= h:
            return 0
        if x == y == 1:
            return 1
        if (x, y) in memo:
            return memo[x, y]
        memo[x, y] = res = P(x - 1, y) / 2 + P(x, y - 1) / 2
        return res

    for q in range(II()):
        w, h, l, u, r, d = MI()
        ans = sum(P(r, y) for y in range(1, u)) / 2 + sum(P(x, d)
                                                          for x in range(1, l)) / 2

        print("Case #{}: {}".format(q + 1, ans))

main()

# passed
from math import log2

def main():
    def P(x, y):
        if x + 1 == w or y + 1 == h:
            return 0
        e = fac[x + y] - fac[x] - fac[y] - x - y
        return pow(2, e)

    fac = [0]
    for i in range(1, 200005):
        fac.append(fac[-1] + log2(i))
    for q in range(II()):
        w, h, l, u, r, d = MI()
        ans = sum(P(r - 1, y) for y in range(u - 1)) / 2 + \
            sum(P(x, d - 1) for x in range(l - 1)) / 2

        print("Case #{}: {}".format(q + 1, ans))

main()

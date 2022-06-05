# solution : https://codingcompetitions.withgoogle.com/kickstart/submissions/000000000019ff43/ZXhvamkyZQ
"""
input:
4
4 6
ZOAAMM
ZOAOMM
ZOOOOM
ZZZZOM
4 4
XXOO
XFFO
XFXO
XXXO
5 3
XXX
XPX
XXX
XJX
XXX
3 10
AAABBCCDDE
AABBCCDDEE
AABBCCDDEE

output:
Case #1: ZOAM
Case #2: -1
Case #3: -1
Case #4: EDCBA
"""
def solve(G):
    R, C = len(G), len(G[0])
    figs = set(''.join(''.join(l) for l in G))
    used = []

    while figs:
        found = False

        for c in figs:
            fail = False

            for x in range(R-1):
                for y in range(C):
                    if G[x][y] == c:
                        if G[x+1][y] != c and G[x+1][y] not in used:
                            fail = True
                            break

            if not fail:
                found = True
                figs.remove(c)
                used.append(c)
                break

        if not found:
            return '-1'

    return ''.join(used)

test = int(input())
for t in range(1, test+1):
    r, c = list(map(int, input().strip().split()))
    G = [list(input()) for _ in range(r)]
    ans = solve(G)
    print("Case #" + str(t) + ": " + str(ans))

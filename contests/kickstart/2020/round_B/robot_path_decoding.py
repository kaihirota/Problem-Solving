import re

test = int(input())
for t in range(1, test+1):

    arr = list(input().strip())
    mvmt = {'N': 0, 'S': 0, 'W': 0, 'E': 0}
    multiplier = 1
    multipliers = []

    # parse command
    for i in range(len(arr)):

        if arr[i] in mvmt:
            mvmt[arr[i]] += 1 * multiplier

        elif arr[i].isdecimal():
            match = re.match('\d+', "".join(arr[i:]))
            start, end = match.span()
            multipliers.append(int(match.group(0)))
            multiplier *= int(match.group(0))

            # skip to end of decimal and parenthesis
            i += (end - start)

        elif arr[i] == ')':
            multiplier = multiplier // multipliers[-1]
            multipliers.pop()

    # calculate mvmt and don't let wh go negative
    x = (mvmt['E'] - mvmt['W']) % 10**9
    y = (mvmt['S'] - mvmt['N']) % 10**9
    print("Case #" + str(t) + ": " + str(x+1), str(y+1))

# simpler solution from someone else's submission
T = int(input())
mod = int(1e9)
for tc in range(1, T+1):
    r = c = 0
    d = 1
    p = []
    for i, v in enumerate(input().strip()):
        if v == 'N':
            r = (r-d)%mod
        elif v == 'S':
            r = (r+d)%mod
        elif v == 'W':
            c = (c-d)%mod
        elif v == 'E':
            c = (c+d)%mod
        elif v == ')':
            d //= p.pop()
        elif v == '(':
            pass
        else:
            t = int(v)
            d *= t
            p.append(t)
    print("Case #" + str(tc) + ":", c+1, r+1)

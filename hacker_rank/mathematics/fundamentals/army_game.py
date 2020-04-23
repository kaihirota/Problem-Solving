def gameWithCells(n, m):
    f = lambda x: x // 2 + x % 2
    return f(n) * f(m)


print(gameWithCells(2, 2))

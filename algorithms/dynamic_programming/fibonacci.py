# top-down DP with memoization using LRU-Cache
from functools import lru_cache

@lru_cache(maxsize=None)
def fib1(n: int) -> int:
    if n <= 2:
        num = 1
    else:
        num = fib1(n-1) + fib1(n-2)
    return num

# bottom-up DP
def fib2(n: int) -> int:
    fib = {}

    for k in range(1, n+1):
        if k <= 2:
            num = 1
        else:
            num = fib[k-1] + fib[k-2]

        fib[k] = num
    return fib[n]

# bottom-up DP constant space
def fib3(n: int) -> int:
    fib = {}

    for k in range(1, n+1):
        if k <= 2:
            num = 1
        else:
            num = fib[k-1] + fib[k-2]
            del fib[k-2]

        fib[k] = num
    return fib[n]

if __name__ == "__main__":
    n = 20
    assert fib1(n) == fib2(n) == fib3(n)

# solution using memoization
results = {}

def fib(n, results):
    try:
        if results[n] != None:
            return results[n]
    except:
        if n == 1 or n == 2:
            return 1
        else:
            result = fib(n-1, results) + fib(n-2, results)
            results[n] = result
            return result


# my version

def fib(n, memo=None):
    if memo == None:
        memo = {}

    if n <= 1:
        return n

    if n not in memo.keys():
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


def getNthFib(n):
    return fib(n-1)

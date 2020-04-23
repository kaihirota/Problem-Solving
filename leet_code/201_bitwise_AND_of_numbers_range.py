"""
201. Bitwise AND of Numbers Range
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
"""
# solution 1: too slow
from functools import reduce
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        return reduce(lambda x, y: x & y, range(m, n+1))


# solution 2
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        counter = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            counter += 1
            # print(i, m, n)
        return n << counter


m = 20
for n in range(21, 40):
    x = Solution().rangeBitwiseAnd(m, n)
    if x > 0:
        print(f'm = {m} {bin(m)[2:].zfill(6)}')
        print(f'n = {n} {bin(n)[2:].zfill(6)} -> {x}')
        print('')

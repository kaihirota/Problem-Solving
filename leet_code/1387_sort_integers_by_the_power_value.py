"""
1387. Sort Integers by The Power Value
https://leetcode.com/problems/sort-integers-by-the-power-value/

The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

if x is even then x = x / 2
if x is odd then x = 3 * x + 1
For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, if two or more integers have the same power value sort them by ascending order.

Return the k-th integer in the range [lo, hi] sorted by the power value.

Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1 using these steps and that the power of x is will fit in 32 bit signed integer.
"""
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_vals = []

        def getPowerValue(x, power_val = 0):
            if x != 1:
                if x % 2 == 0:
                    return getPowerValue(x / 2, power_val+1)
                else:
                    return getPowerValue(3 * x + 1, power_val+1)
            else:
                return power_val

        for i in range(lo, hi+1):
            p = getPowerValue(i)
            power_vals += (i, p),

        power_vals.sort(key=lambda x: (x[1], x[0]))
        return power_vals[k-1][0]

assert Solution().getKth(lo = 12, hi = 15, k = 2) == 13

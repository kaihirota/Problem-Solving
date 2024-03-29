"""
338. Counting Bits
https://leetcode.com/problems/counting-bits/

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""

from typing import List

# class Solution:
#     def countBits(self, num: int) -> List[int]:
#         ret = []
#         for i in range(num+1):
#             bits = map(int, list(bin(i)[2:]))
#             ret.append(sum(bits))
#         return ret

# solution
class Solution(object):
    """Code works by constantly extending a list with itself but with the values incremented by 1."""
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]
        while len(res) <= num:
            res += [i+1 for i in res]
        return res[:num+1]


print(Solution().countBits(num=20))

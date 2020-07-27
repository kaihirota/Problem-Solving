"""
922. Sort Array By Parity II
https://leetcode.com/problems/sort-array-by-parity-ii/
"""
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = [i for i in A if i % 2 == 0]
        odd = [i for i in A if i % 2 != 0]
        ret = []
        for i in range(len(A)):
            if i % 2 == 0:
                ret += even.pop(),
            else:
                ret += odd.pop(),
        return ret

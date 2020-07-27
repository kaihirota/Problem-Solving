"""
961. N-Repeated Element in Size 2N Array
https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
"""
from collections import defaultdict

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        counter = defaultdict(int)
        n = len(A)
        for i in range(n):
            counter[A[i]] += 1
            if counter[A[i]] == n // 2:
                return A[i]

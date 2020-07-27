class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        counter = 0
        for i in range(1, n+1):
            if n % i == 0:
                counter += 1
                if counter == k:
                    return i
        return -1


assert Solution().kthFactor(n = 12, k = 3) == 3
"""
Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
"""

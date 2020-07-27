from typing import List

class Solution:
    # def numOfSubarrays(self, arr: List[int]) -> int:
    #     dp = [[0] * len(arr) for i in range(len(arr))]
    #     dp[0][0] = arr[0]
    #     counter = 0
    #     if len(arr) == 1:
    #         return int(arr[0] % 2 != 0)
    #     for i in range(len(arr)):
    #         for j in range(i, len(arr)):
    #             dp[i][j] = dp[i][j-1] + arr[j]
    #             if dp[i][j] % 2 != 0:
    #                 counter += 1
    #     return counter % (10**9 + 7)
    def numOfSubarrays(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            curr_sum = arr[i]
            j = i + 1
            while curr_sum + arr[j] 


assert Solution().numOfSubarrays(arr = [1,3,5]) == 4
assert Solution().numOfSubarrays(arr = [2,4,6]) == 0
assert Solution().numOfSubarrays(arr = [3,4]) == 2
assert Solution().numOfSubarrays(arr = [1,2,3,4,5,6,7]) == 16
assert Solution().numOfSubarrays(arr = [100,100,99,99]) == 4
assert Solution().numOfSubarrays(arr = [7]) == 1

from typing import *

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        i, j = 0, len(nums) - 1
        ops = 0
        while i < j:
            if nums[i] + nums[j] > k:
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                ops += 1
                j -= 1
                i += 1
        return ops


print(Solution().maxOperations(nums = [1,2,3,4], k = 5))
print(Solution().maxOperations(nums = [3,1,3,4,3], k = 6))
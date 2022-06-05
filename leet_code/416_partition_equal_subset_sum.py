"""
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Notes:
- Since we can assume non-empty array with positive integers, and because we are dealing with 
  only 2 partitions, we can use the heuristic
    - if the array can be partitioned into two and have the same sum, that means each of the partition's sum will be half of the total sum of the original array
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)
        subset_sum = total_sum // 2

        if total_sum % 2 != 0:
            return False

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (n + 1) for _ in range(subset_sum + 1)]
        dp[0][0] = True
        for k in range(subset_sum + 1):
            for j in range(1, n + 1):
                if k >= nums[j - 1]:
                    dp[k][j] = dp[k][j - 1] or dp[k - nums[j - 1]][j - 1]
                else:
                    dp[k][j] = dp[k][j - 1]

        for row in dp:
            print(row)
        return dp[subset_sum][n]

# assert Solution().canPartition([1,5,11,5]) == True
# assert Solution().canPartition([1,2,3,5]) == False
assert Solution().canPartition([1,2,4,5]) == True
# assert Solution().canPartition([8,7,13,2]) == True
# assert Solution().canPartition([1,5,3]) == False
# assert Solution().canPartition([1,2,3,4,5,6,7]) == True
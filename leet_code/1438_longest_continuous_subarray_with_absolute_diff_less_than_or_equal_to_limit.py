"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

Given an array of integers nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.

In case there is no subarray satisfying the given condition return 0.



Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""
from typing import List
from collections import deque
class Solution:
    # TLE
    # def longestSubarray(self, nums: List[int], limit: int) -> int:
    #     if not nums:
    #         return 0
    #
    #     dp = [1] * len(nums)
    #
    #     for i in range(len(nums)):
    #         maxn = float('-inf')
    #         minn = float('inf')
    #
    #         for j in range(i, len(nums)):
    #             maxn = max(maxn, nums[j], nums[i])
    #             minn = min(minn, nums[j], nums[i])
    #
    #             if maxn - minn <= limit:
    #                 dp[j] = max(dp[j], j+1-i)
    #
    #     return max(dp)

    # solution
    # Time O(N)
    # Space O(N)
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxd = deque()
        mind = deque()
        i = 0

        for j, a in enumerate(nums):
            print(j, a, maxd, mind)
            while len(maxd) and a > maxd[-1]: maxd.pop()
            while len(mind) and a < mind[-1]: mind.pop()

            maxd.append(a)
            mind.append(a)

            if maxd[0] - mind[0] > limit:
                if maxd[0] == nums[i]: maxd.popleft()
                if mind[0] == nums[i]: mind.popleft()
                i += 1

        return j - i + 1


assert Solution().longestSubarray(nums = [8,2,4,7], limit = 4) == 2
assert Solution().longestSubarray(nums = [10,1,2,4,7,2], limit = 5) == 4
assert Solution().longestSubarray(nums = [4,2,2,2,4,4,2,2], limit = 0) == 3

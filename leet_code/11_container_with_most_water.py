"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
"""
from typing import List
class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     dp = [0] * len(height)
    #     for i in range(len(height)-1):
    #         for j in range(i+1, len(height)):
    #             dp[i] = max(dp[i], min(height[i], height[j]) * abs(i-j))
    #     return max(dp)

    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        curr_area = 0

        while l < r:
            if height[l] > height[r]:
                area = height[r] * (r - l)
                r -= 1
            else:
                area = height[l] * (r - l)
                l += 1
            curr_area = max(curr_area, area)

        return curr_area


assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert Solution().maxArea([1,2]) == 1
assert Solution().maxArea([1,2,1]) == 2
assert Solution().maxArea([1,2,4,3]) == 4

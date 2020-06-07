"""
https://leetcode.com/problems/maximum-subarray/

53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

solution: Kadane's Algorithm
"""

class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums):
        current_max = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            current_max = max(nums[i], nums[i] + current_max)

            if current_max > global_max:
                global_max = current_max

        return global_max

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

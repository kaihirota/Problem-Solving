"""
https://leetcode.com/problems/first-missing-positive/

41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1

        for idx in range(len(nums)):
            while 1 <= nums[idx] <= len(nums):
                if nums[nums[idx]-1] == nums[idx]:
                    break
                nums[nums[idx]-1], nums[idx] = nums[idx], nums[nums[idx]-1]

        for idx, elem in enumerate(nums):
            if idx + 1 != elem:
                return idx + 1

        return len(nums) + 1

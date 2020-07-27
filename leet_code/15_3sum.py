"""
15. 3Sum
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
# from collections import defaultdict
# from typing import List
#
#
# class Solution:
#     # TLE
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         sums = defaultdict(list)
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i != j:
#                     sums[nums[i] + nums[j]] += [i, j],
#
#         ret = set()
#         for idx, num in enumerate(nums):
#             if -num in sums:
#                 for i, j in sums[-num]:
#                     if idx != i and idx != j:
#                         ret.add(tuple(sorted([nums[i], nums[j], num])))
#         return [list(item) for item in ret]
#

class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

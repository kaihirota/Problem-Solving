"""
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

"""
class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
    def findMaxLength(self, nums):
        d = {0: 0}
        key, maxL = 0, 0
        for i in range(len(nums)):
            key += nums[i] or -1
            if key not in d:
                d[key] = i+1
            else:
                maxL = max(maxL, i+1-d[key])
        return maxL

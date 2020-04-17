"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
from functools import reduce

class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
    def productExceptSelf(self, nums):
        if 0 in nums:
            ret = [0] * len(nums)
            if len(list(filter(lambda x: x == 0, nums))) == 1:
                zero_i = nums.index(0)
                nums.pop(zero_i)
                ret[zero_i] = reduce(lambda x, y: x * y, nums)
        else:
            ret = [reduce(lambda x, y: x * y, nums[1:])]

            for i in range(1, len(nums)):
                ret.append(ret[0] // nums[i] * nums[0])

        return ret


# solution
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

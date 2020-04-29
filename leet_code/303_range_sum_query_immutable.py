"""
303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
Accepted
186,449
Submissions
434,743
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] = self.nums[i] + self.nums[i-1]


    def sumRange(self, i: int, j: int) -> int:
        if i == j and i == 0:
            return self.nums[i]
        elif i == j and i > 0:
            return self.nums[i] - self.nums[i-1]
        elif i == 0 and j > 0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

"""
https://leetcode.com/problems/find-all-duplicates-in-an-array/

442. Find All Duplicates in an Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []

        for idx in range(len(nums)):
            while nums[idx] != idx + 1:
                if nums[nums[idx]-1] == nums[idx]:
                    break
                nums[nums[idx]-1], nums[idx] = nums[idx], nums[nums[idx]-1]

        for idx, elem in enumerate(nums):
            if idx + 1 != elem:
                ret.append(elem)

        return ret

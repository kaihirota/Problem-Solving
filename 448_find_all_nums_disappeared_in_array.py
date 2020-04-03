"""
448. Find All Numbers Disappeared in an Array

https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

approach 1: hash map

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in s]

approach 2: smart sort
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:            
        ret = []

        for idx in range(len(nums)):
            while nums[idx] != idx + 1:
                if nums[nums[idx]-1] == nums[idx]:
                    break
                nums[nums[idx]-1], nums[idx] = nums[idx], nums[nums[idx]-1]

        for idx, elem in enumerate(nums):
            if idx + 1 != elem:
                ret.append(idx+1)

        return ret

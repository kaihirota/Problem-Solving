"""
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/
"""
from collections import defaultdict
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = defaultdict(int)
        for i in range(len(nums1)):
            nums[nums1[i]] = 1
        for i in range(len(nums2)):
            if nums2[i] in nums:
                nums[nums2[i]] = 2
        return [i for i in nums.keys() if nums[i] > 1]

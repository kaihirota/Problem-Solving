"""
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.
"""
from collections import Counter
from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        nums = set(nums1).union(set(nums2))

        ret = []
        for num in nums:
            if num in c1 and num in c2:
                ret += [num] * min([c1[num], c2[num]])
        return ret


print(Solution().intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
print(Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]))
print(Solution().intersect(nums1 = [4,4,1,9,9,9,5], nums2 = [9,4,9,8,4,5]))

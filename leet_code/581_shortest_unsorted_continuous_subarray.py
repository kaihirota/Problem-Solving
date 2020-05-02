"""
581. Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""
from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        start = None
        end = None

        if nums == nums2:
            return 0

        for i in range(len(nums)):
            if nums[i] != nums2[i]:
                if start == None:
                    start = i
                elif end == None:
                    end = i
                else:
                    end = max(end, i)

        return end - start + 1


nums = [2, 6, 4, 8, 10, 9, 15]
assert Solution().findUnsortedSubarray(nums) == 5

nums = [1,2,3,4]
print(Solution().findUnsortedSubarray(nums))

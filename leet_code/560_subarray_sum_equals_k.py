"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

"""
from typing import List
from collections import defaultdict, Counter
from itertools import accumulate

# solution 1 - TimeLimitExceeded
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumsum = defaultdict(int)
        counter = 0

        for i, elem in enumerate(nums):
            for j in range(i+1):
                cumsum[j] += elem

                if cumsum[j] == k:
                    counter += 1

        return counter

# solution 2 - TimeLimitExceeded
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        for i in range(1, len(nums)):
            if nums[i] == k:
                counter +=1
            nums[i] = nums[i-1] + nums[i]

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] == k:
                    counter += 1
        return counter

# solution 3 - linear time, pass
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter()
        counter[0] += 1
        total = 0

        for cumsum in accumulate(nums):
            total += counter[cumsum - k]
            counter[cumsum] += 1

        return total


# nums = [1, 4, 3, 2, -2, 5, -1, 2, 1, 2]
nums = [1, 1, 1]
k = 2
"""
1, 4
3, 2
2, -2, 5
5
-2, 5, -1, 2, 1
2, 1, 2
"""
result = Solution().subarraySum(nums, k)
print(result)

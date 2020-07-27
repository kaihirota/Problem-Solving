"""
78. Subsets
https://leetcode.com/problems/subsets/

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Let's start from empty subset in output list. At each step one takes new integer into consideration and generates new subsets from the existing ones.
        """
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]
        return output


Solution().subsets([1, 2, 3])

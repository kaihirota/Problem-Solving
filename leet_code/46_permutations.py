"""
46. Permutations
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
from collections import deque
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def BFS(choices, permutation=[]):
            if len(permutation) < len(nums):
                for i in range(len(choices)):
                    choice = choices.pop()
                    permutation.append(choice)
                    BFS(choices, [i for i in permutation])
                    choices.appendleft(choice)
                    permutation.pop()
            else:
                permutations.append(permutation)

        BFS(choices=deque(nums))
        return permutations


print(Solution().permute([1,2,3]))

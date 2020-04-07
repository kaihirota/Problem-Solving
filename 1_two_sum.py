"""
https://leetcode.com/problems/two-sum/

1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Input [3,3], 6
Output []
Expected [0,1]
"""

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums: list, target: int):

        d = {}
        """
        {
            "3": [0, 1],
            "1": [2]
        }
        """
        for i, elem in enumerate(nums):

            if str(elem) in d.keys():
                d[str(elem)].append(i)
            else:
                d[str(elem)] = [i]


        for elem, i in d.items():
            g = target - int(elem)

            if str(g) in d.keys():
                if len(d[str(g)]) == 2:
                    return d[str(g)]
                elif elem != str(g):
                    return [d[str(g)][0], i[0]]

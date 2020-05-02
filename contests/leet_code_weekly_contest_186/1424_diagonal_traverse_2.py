"""
1424. Diagonal Traverse II
https://leetcode.com/problems/diagonal-traverse-ii/

Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.


Example 1:



Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:



Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
Example 3:

Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
Output: [1,4,2,5,3,8,6,9,7,10,11]
Example 4:

Input: nums = [[1,2,3,4,5,6]]
Output: [1,2,3,4,5,6]


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
There at most 10^5 elements in nums.
"""

from typing import List
import collections

# # time limit exceeded
# class Solution:
#     def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
#         n = len(nums)
#         ret = []
#         i = 0
#         diagonal_range = 0
#         while True:
#             if nums[i]:
#                 item = nums[i].pop(0)
#                 ret.append(item)
#
#             if i == 0:
#                 if diagonal_range < n - 1:
#                     diagonal_range += 1
#                 i = diagonal_range
#             else:
#                 i -= 1
#
#             if max([len(row) for row in nums]) == 0:
#                 return ret
#
#         return ret

# Solution
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # we create a dic indexed by sum i+j, as all items in a diagonal will have the same sum.
        diagonals = collections.defaultdict(list)

        # traverse from top row to bottom; we can see this is reversed order compared to our desired result.
        for i, line in enumerate(nums):
            for j in range(len(line)):
                diagonals[i+j].append(line[j]) # add the element to the correct bucket.
                """
                diagonals = defaultdict({
                                0: [1],
                                1: [2, 4],
                                2: [3, 5, 7],
                                3: [6, 8],
                                4: [9]
                })"""

        i = 0
        ret = []

        # we now reverse the buckets and concatenate them to get the result.
        while i in diagonals:
            ret.extend(diagonals[i][::-1])
            i += 1
        return ret

nums = [[1,2,3],[4,5,6],[7,8,9]]
output = [1,4,2,7,5,3,8,6,9]
print(Solution().findDiagonalOrder(nums = nums) == output)

# nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
# output = [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
# print(Solution().findDiagonalOrder(nums = nums) == output)

"""
1198. Find Smallest Common Element in All Rows
https://leetcode.com/problems/find-smallest-common-element-in-all-rows/
"""
from collections import defaultdict
from typing import List
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        nums = defaultdict(int)
        n_rows = len(mat)
        for i in range(n_rows):
            row_member = set()
            for j in range(len(mat[0])):
                if mat[i][j] not in row_member:
                    row_member.add(mat[i][j])
                    nums[mat[i][j]] += 1
        for key in sorted(nums.keys()):
            if nums[key] == n_rows:
                return key
        return -1


assert Solution().smallestCommonElement(mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]) == 5

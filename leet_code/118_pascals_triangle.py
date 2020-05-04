"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = [[1] * i for i in range(1, numRows+1)]

        if numRows > 2:
            for i in range(2, numRows):
                for j in range(1, i):
                    tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

        return tri


    """
    Solution
    Any row can be constructed using the offset sum of the previous row. Example:

       1 3 3 1 0
    +  0 1 3 3 1
    =  1 4 6 4 1
    """
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:numRows]


print(Solution().generate(numRows=5))

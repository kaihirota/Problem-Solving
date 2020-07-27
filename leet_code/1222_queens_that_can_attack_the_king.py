"""
1222. Queens That Can Attack the King
https://leetcode.com/problems/queens-that-can-attack-the-king/

On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of the Black Queens, and a pair of coordinates king that represent the position of the White King, return the coordinates of all the queens (in any order) that can attack the King.
"""
from typing import List
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set([(x, y) for x, y in queens])
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        check = []

        for dx, dy in directions:
            x, y = king
            while 0 <= x < 8 and 0 <= y < 8 and (x, y) not in queens:
                x += dx
                y += dy

            if (x, y) in queens:
                check += (x, y),

        return check


queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
king = [0,0]
Solution().queensAttacktheKing(queens, king)
# Output: [[0,1],[1,0],[3,3]]

# queens =[
#     [5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],
#     [0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],
#     [0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]
# ]
# king = [3,4]
# Solution().queensAttacktheKing(queens, king)
# Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]

"""
1411. Number of Ways to Paint N × 3 Grid
https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

User Accepted:441
User Tried:489
Total Accepted:455
Total Submissions:616
Difficulty:Hard

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 2:

Input: n = 2
Output: 54
Example 3:

Input: n = 3
Output: 246
Example 4:

Input: n = 7
Output: 106494
Example 5:

Input: n = 5000
Output: 30228214

Constraints:
n == grid.length
grid[i].length == 3
1 <= n <= 5000
"""
class Solution:
    def numOfWays(self, n):
        a121, a123 = 6, 6

        for i in range(n-1):
            a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2

        mod = 10**9 + 7
        return (a121 + a123) % mod

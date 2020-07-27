"""
289. Game of Life
https://leetcode.com/problems/game-of-life/

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
"""
from collections import defaultdict
from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        prev_state = defaultdict(int)

        for i in range(m):
            for j in range(n):
                prev_state[(i, j)] = board[i][j]

        neighbors = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]

        for i in range(m):
            for j in range(n):

                live_neighbors = sum([prev_state[(i+dx, j+dy)] for dx, dy in neighbors])

                if prev_state[(i, j)] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 0
                    else:
                        continue
                else:
                    if live_neighbors == 3:
                        board[i][j] = 1

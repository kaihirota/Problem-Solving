"""
243. Shortest Word Distance
https://leetcode.com/problems/shortest-word-distance/
"""
from typing import List
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        shortest = float('inf')
        for i in range(len(words)):
            if words[i] == word1:
                for j in range(len(words)):
                    if words[j] == word2:
                        shortest = min(shortest, abs(i-j))
        return shortest

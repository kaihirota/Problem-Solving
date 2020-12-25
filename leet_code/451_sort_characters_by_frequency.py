"""
451. Sort Characters By Frequency
https://leetcode.com/problems/sort-characters-by-frequency/
"""
from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1

        ret = ''
        for char, occ in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            ret += char * occ
        return ret

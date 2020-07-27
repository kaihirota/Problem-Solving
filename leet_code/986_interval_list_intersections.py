"""
986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/
"""
from collections import deque
from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if len(A) == 0 or len(B) == 0:
            return None

        A.extend(B)
        intervals = deque(sorted(A))

        curr = intervals.popleft()
        ret = []

        while intervals:
            start, end = intervals.popleft()

            if curr[0] <= start and curr[1] >= end:
                ret += [start, end],
            elif curr[1] >= start:
                ret += [start, curr[1]],

            if end > curr[1]:
                curr = [start, end]

        return ret


Solution().intervalIntersection(A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]])
Solution().intervalIntersection(A = [[3,5],[9,20]], B = [[4,5],[7,10],[11,12],[14,15],[16,20]])

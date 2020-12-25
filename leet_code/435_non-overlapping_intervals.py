"""
435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
"""
from typing import List
from collections import deque
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        intervals = deque(intervals)

        if len(intervals) <= 1:
            return 0

        curr = intervals.popleft()
        ret = 0

        while intervals:
            interval = intervals.popleft()
            if curr[1] <= interval[0]:
                curr[1] = interval[1]
            else:
                ret += 1
        return ret


assert Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
assert Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
assert Solution().eraseOverlapIntervals([[1,2],[2,3]]) == 0

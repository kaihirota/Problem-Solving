"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
Given a collection of intervals, merge all overlapping intervals.
"""
from collections import deque
from typing import List
class Solution:
    # def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    #     maxnum = 0
    #     for start, end in intervals:
    #         maxnum = max(maxnum, end)
    #     arr = [0] * (maxnum + 1)
    #
    #     for start, end in intervals:
    #         for i in range(start, end):
    #             arr[i] = 1
    #
    #     ret = []
    #     for i in range(len(arr)):
    #         start = end = i
    #         while i < len(arr) and arr[i] == 1:
    #             arr[i] = 0
    #             end = i
    #             i += 1
    #
    #         if start != end:
    #             ret += [start, end],
    #     return ret
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals
        intervals.sort(key=lambda x: x[0])
        intervals = deque(intervals)
        interval = intervals.popleft()
        merged = [interval]

        while intervals:
            start, end = intervals.popleft()
            if merged[-1][1] >= start and merged[-1][1] < end:
                merged[-1][1] = end
            elif merged[-1][1] >= start and merged[-1][1] >= end:
                continue
            else:
                merged += [start, end],
        return merged


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[1,4],[2,3]]))

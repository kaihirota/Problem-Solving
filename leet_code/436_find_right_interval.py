"""
436. Find Right Interval
https://leetcode.com/problems/find-right-interval/
"""
from typing import List
class Solution:
    # def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    #     ret = [[-1, float('inf')]] * len(intervals)
    #     for i in range(len(intervals)):
    #         for j in range(len(intervals)):
    #             if i != j and intervals[i][1] <= intervals[j][0]:
    #                 ret[i] = min(ret[i], [j, intervals[j][0] - intervals[i][1]], key=lambda x: x[1])
    #
    #     ret = [item[0] for item in ret]
    #     return ret
    # def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
    #     intervals = [[start, end, idx, -1] for idx, (start, end) in enumerate(intervals)]
    #     print(intervals[8])
    #     intervals.sort(key=lambda x: (x[1], x[0]))
    #     print(intervals)
    #
    #     for i in range(len(intervals)-1):
    #         for j in range(i+1, len(intervals)):
    #             if intervals[i][1] <= intervals[j][0]:
    #                 intervals[i][3] = intervals[j][2]
    #                 break
    #
    #     intervals.sort(key=lambda x: x[2])
    #     # print(intervals)
    #     return [j for start, end, idx, j in intervals]
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        mapping = {start : idx for idx, (start, end) in enumerate(intervals)}
        max_num = max(mapping.keys())
        ret = []

        for start, end in intervals:
            num = end
            while num not in mapping and num <= max_num:
                num += 1

            if num > max_num:
                ret += -1,
            else:
                ret += mapping[num],
        return ret

assert Solution().findRightInterval([ [3,4], [2,3], [1,2] ]) == [-1, 0, 1]
assert Solution().findRightInterval([ [1,4], [2,3], [3,4] ]) == [-1, 2, -1]

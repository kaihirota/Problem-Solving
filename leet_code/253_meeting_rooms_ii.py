"""
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/
"""
from typing import List
import heapq

class Solution:
    # def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    #     if len(intervals) == 0:
    #         return 0
    #
    #     n = max([end for start, end in intervals])
    #     arr = [0] * (n + 1)
    #     for start, end in intervals:
    #         for i in range(start, end):
    #             arr[i] += 1
    #     return max(arr)

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:
                # If the new start time >= existing end time, the room has been released. Replace the previous time with the new ending time
                heapq.heapreplace(heap, end)
            else:
                # The room is still in use, add (push a new end time to min heap) a new room
                heapq.heappush(heap, end)
        return len(heap)


assert Solution().minMeetingRooms([[0, 30],[5, 10],[15, 20]]) == 2
assert Solution().minMeetingRooms([[7,10],[2,4]]) == 1
assert Solution().minMeetingRooms([[13,15],[1,13]]) == 1

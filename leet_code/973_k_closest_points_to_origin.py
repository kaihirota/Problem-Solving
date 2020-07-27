"""
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)
"""
import heapq
import math
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        closest = []
        for x, y in points:
            heapq.heappush(closest, (math.sqrt(x**2 + y**2), (x, y)))
        return [heapq.heappop(closest)[1] for i in range(K)]

Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2)

"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""
from queue import PriorityQueue
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = PriorityQueue()
        for i in range(len(nums)):
            queue.put(-nums[i])

        return [queue.get() * -1 for i in range(k)][-1]


Solution().findKthLargest([3,2,1,5,6,4], 2)
Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)

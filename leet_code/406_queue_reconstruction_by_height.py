"""
406. Queue Reconstruction by Height
https://leetcode.com/problems/queue-reconstruction-by-height/

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
from collections import defaultdict
from typing import List

class Solution(object):
    def reconstructQueue(self, people):
        people_dct = defaultdict(list)
        res = []

        # dictionary to capture one-to-many relationship of height to people
        # record index for later use
        for idx, (height, taller) in enumerate(people):
            people_dct[height] += (taller, idx),

        # sort by height in decreasing order, and then sort by the number of taller people to the left (in front of queue)
        for height in sorted(people_dct.keys(), reverse=True):
            for taller, idx in sorted(people_dct[height]):
                res.insert(taller, people[idx])

        return res

people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
assert Solution().reconstructQueue(people) == [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

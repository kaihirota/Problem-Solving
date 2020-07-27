"""
1104. Path In Zigzag Labelled Binary Tree
https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.
"""
from math import log2, pow, ceil
from typing import List

class Solution:
    # def pathInZigZagTree(self, label: int) -> List[int]:
    #
    #     level = ceil(log2(label+1))
    #     heap = []
    #     current_pos = None
    #
    #     for lv in range(level, 0, -1):
    #
    #         if lv % 2 == 0:
    #             start = int(pow(2, lv) - 1)
    #             stop = int(pow(2, lv - 1) - 1)
    #             increment = -1
    #         else:
    #             start = int(pow(2, lv - 1))
    #             stop = int(pow(2, lv))
    #             increment = 1
    #
    #         layer = list(range(start, stop, increment))
    #
    #         if current_pos is None:
    #             current_pos = layer.index(label)
    #
    #         heapq.heappush(heap, layer[current_pos])
    #         current_pos = current_pos // 2
    #
    #     path = []
    #     for i in range(len(heap)):
    #         path += heapq.heappop(heap),
    #     return path

    def pathInZigZagTree(self, label: int) -> List[int]:

        level = ceil(log2(label+1))
        nums = list(range(int(pow(2, level))))
        path = []

        if level % 2 == 0:
            current_pos = int(pow(2, level)) - label - 1
        else:
            current_pos = label - int(pow(2, level-1))

        while level > 0:
            slice = len(nums) // 2
            curr_layer = nums[slice:]

            if level % 2 == 0:
                path += curr_layer[-current_pos-1],
            else:
                path += curr_layer[current_pos],

            nums = nums[:slice]
            level -= 1
            current_pos = current_pos // 2

        return path[::-1]


assert Solution().pathInZigZagTree(label = 14) == [1,3,4,14]
assert Solution().pathInZigZagTree(label = 26) == [1,2,6,10,26]

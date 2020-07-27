"""
1161. Maximum Level Sum of a Binary Tree
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
"""
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levelSum = defaultdict(int)

        def DFS(root: TreeNode, level: int):
            if root:
                levelSum[level] += root.val

                for node in [root.left, root.right]:
                    if node:
                        DFS(node, level=level+1)


        DFS(root, level=1)

        maxVal = (1, root.val)
        for level in levelSum.keys():
            maxVal = max(maxVal, (level, levelSum[level]), key=lambda x: x[1])
        return maxVal[0]



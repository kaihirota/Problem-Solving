"""
987. Vertical Order Traversal of a Binary Tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""
from typing import List
from collections import defaultdict
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.ret = defaultdict(list)

        def DFS(node, x=0, y=0):
            if node:
                self.ret[x] += (node.val, y),
                DFS(node.left, x-1, y-1)
                DFS(node.right, x+1, y-1)

        DFS(root)
        nodes = [[(x, y, val) for val, y in self.ret[x]] for x in sorted(self.ret.keys())]
        for i in range(len(nodes)):
            nodes[i].sort(key=lambda x: (x[0], -x[1], x[2]))
        return [[val for x, y, val in node] for node in nodes]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().verticalTraversal(root))

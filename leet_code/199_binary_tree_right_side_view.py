"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
"""
from collections import defaultdict
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def rightSideView(self, root: TreeNode) -> List[int]:
    #     self.ret = defaultdict(tuple)
    #     def DFS(node: TreeNode, depth: int=0, pos: int=0):
    #         if node and node.val:
    #             self.ret[depth] = max(self.ret[depth], (pos, node.val))
    #             DFS(node.left, depth+1, pos-1)
    #             DFS(node.right, depth+1, pos+1)
    #
    #     DFS(root)
    #     return [self.ret[depth][1] for depth in sorted(self.ret.keys())]
    def rightSideView(self, root: TreeNode) -> List[int]:
        def DFS(node: TreeNode, depth: int=0):
            if node:
                if depth == len(ret):
                    ret.append(node.val)
                DFS(node.right, depth+1)
                DFS(node.left, depth+1)


        ret = []
        DFS(root)
        return ret


root = TreeNode(1)
root.left = TreeNode(1)
root.left.left = TreeNode(1)
root.left.left.left = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(3)
print(Solution().rightSideView(root))

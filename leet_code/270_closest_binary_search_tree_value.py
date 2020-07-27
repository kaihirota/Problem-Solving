"""
270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root:

            self.closest = root.val
            self.target = target
            def DFS(root):
                if root:
                    self.closest = min(self.closest, root.val, key=lambda x: abs(target - x))
                    DFS(root.left)
                    DFS(root.right)
            DFS(root)
            return self.closest

    def closestValue(self, root, target):
        a = root.val

        kid = root.left if target < a else root.right
        if not kid:
            return a

        b = self.closestValue(kid, target)
        return min((b, a), key=lambda x: abs(target - x))

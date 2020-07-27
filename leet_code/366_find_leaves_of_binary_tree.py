"""
366. Find Leaves of Binary Tree
https://leetcode.com/problems/find-leaves-of-binary-tree/
"""
from collections import defaultdict
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        leaves = defaultdict(list)
        if not root or root.val == None:
            return None

        def DFS(root, iteration):
            if root:
                if root.left is None and root.right is None:
                    leaves[iteration] += root.val,
                    return True
                else:
                    if DFS(root.left, iteration):
                        root.left = None
                    if DFS(root.right, iteration):
                        root.right = None

        iteration = 0
        while root:
            if DFS(root, iteration):
                break
            iteration += 1

        return [leaves[i] for i in range(iteration+1)]


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# print(Solution().findLeaves(root))
# root = TreeNode(1)
# print(Solution().findLeaves(root))
root = TreeNode(None)
print(Solution().findLeaves(root))

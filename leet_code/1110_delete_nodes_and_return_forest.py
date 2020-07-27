"""
1110. Delete Nodes And Return Forest
https://leetcode.com/problems/delete-nodes-and-return-forest/

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.trees = []
        self.to_delete = set(to_delete)

        def DFS(root):
            if root:
                DFS(root.left)
                DFS(root.right)
                left, right = check(root.left), check(root.right)
                if left:
                    root.left = None
                if right:
                    root.right = None

        def check(root):
            if root:
                if root.val in self.to_delete:
                    for node in [root.left, root.right]:
                        if node:
                            self.trees.append(node)
                    return True
                return False

        DFS(root)
        if check(root) is not True:
            self.trees.append(root)
        return self.trees


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# trees = Solution().delNodes(root, to_delete=[3,5])
# print([tree.val for tree in trees])

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
trees = Solution().delNodes(root, to_delete=[2,1])
print([tree.val for tree in trees])

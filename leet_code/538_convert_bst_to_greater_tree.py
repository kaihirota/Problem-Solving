"""
538. Convert BST to Greater Tree
https://leetcode.com/problems/convert-bst-to-greater-tree/
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        """
        1. calculate sum of all nodes
        2. DFS, start from smallest node and subtract / modify
        """

        # get sum of all nodes
        total = 0
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                total += node.val
                if node.left:
                    stack += node.left,
                if node.right:
                    stack += node.right,

            total = self.DFS(root, total)
            return root


    def DFS(self, root: TreeNode, total):
        if root:
            total = self.DFS(root.left, total)

            value = root.val
            root.val = total
            total -= value
            total = self.DFS(root.right, total)

        return total

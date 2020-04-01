"""
https://leetcode.com/problems/invert-binary-tree/

226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            if root.left and root.right:
                node_pointer = self.invertTree(root.left)
                root.left = self.invertTree(root.right)
                root.right = node_pointer
            elif root.left and not root.right:
                node_pointer = self.invertTree(root.left)
                root.left = root.right
                root.right = node_pointer
            elif root.right and not root.left:
                node_pointer = self.invertTree(root.right)
                root.right = root.left
                root.left = node_pointer
            return root

"""
https://leetcode.com/problems/diameter-of-binary-tree/

543. Diameter of Binary Tree

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_length = 1

        def get_depth(node):
            if not node:
                return 0

            left_len = get_depth(node.left)
            right_len = get_depth(node.right)

            # update if length is greater than max_length
            self.max_length = max(self.max_length, left_len + right_len + 1)

            # return the value of the side that's longer + 1
            return max(left_len, right_len) + 1

        get_depth(root)
        return self.max_length - 1

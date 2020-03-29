# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        merged = TreeNode(t1.val + t2.val)

        if t1.left and t2.left:
            merged.left = self.mergeTrees(t1.left, t2.left)

        elif (t1.left == None)^(t2.left == None):
            # only if one of the two nodes is None
            if t1.left == None:
                merged.left = t2.left
            else:
                merged.left = t1.left

        if t1.right and t2.right:
            merged.right = self.mergeTrees(t1.right, t2.right)
        elif (t1.right == None)^(t2.right == None):
            # only if one of the two nodes is None
            if t1.right == None:
                merged.right = t2.right
            else:
                merged.right = t1.right

        return merged

"""
https://leetcode.com/problems/merge-two-binary-trees/
617. Merge Two Binary Trees

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.

reflection:
After taking a break, I was able to revise my code line by line and slowly but precisely identify what will go wrong. I did this by visualizing edge cases and running mental simulation.
"""

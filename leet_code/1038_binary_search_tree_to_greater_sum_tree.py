"""
1038. Binary Search Tree to Greater Sum Tree
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Constraints:
The number of nodes in the tree is between 1 and 100.
Each node will have value between 0 and 100.
The given tree is a binary search tree.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        1. calculate sum of all nodes
        2. DFS, start from smallest node and subtract / modify
        """

        # get sum of all nodes
        total = 0
        stack = [root]
        while stack:
            node = stack.pop()
            total += node.val
            if node.left:
                stack += node.left,
            if node.right:
                stack += node.right,

        total = self.DFS(root, total)
        print(total)
        print(root.val)


    def DFS(self, root: TreeNode, total):
        if root:
            total = self.DFS(root.left, total)

            value = root.val
            root.val = total
            total -= value
            total = self.DFS(root.right, total)

        return total


root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
Solution().bstToGst(root)

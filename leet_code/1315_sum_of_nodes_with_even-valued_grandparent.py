"""
1315. Sum of Nodes with Even-Valued Grandparent
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

Example 1:
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.DFS(root)


    def DFS(self, root):
        subtotal = 0
        if root:
            subtotal += self.DFS(root.left)
            subtotal += self.DFS(root.right)

            if root.val % 2 == 0:
                subtotal += self.sum_grandchildren(root)

        return subtotal


    def sum_grandchildren(self, root):
        nodes = [root.left, root.right]
        grandchildren = 0
        for node in nodes:
            if node:
                if node.left:
                    grandchildren += node.left.val
                if node.right:
                    grandchildren += node.right.val
        return grandchildren


root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.left.left.left = TreeNode(9)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
print(Solution().sumEvenGrandparent(root = root))

"""
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> 'TreeNode':
    #
    #     def DFS(node, p, q, depth=0):
    #         if node:
    #             if BFS(node, p, q):
    #                 self.lca = max(self.lca, (depth, node))
    #             DFS(node.left, p, q, depth+1)
    #             DFS(node.right, p, q, depth+1)
    #
    #     def BFS(root, p, q):
    #         stack = [root]
    #         p_found = q_found = False
    #         while stack:
    #             node = stack.pop()
    #
    #             for child in [node.left, node.right]:
    #                 if child:
    #                     stack += child,
    #             if node.val == p.val:
    #                 p_found = True
    #             if node.val == q.val:
    #                 q_found = True
    #         if p_found and q_found:
    #             return True
    #         else:
    #             return False
    #
    #     self.lca = (0, root)
    #     DFS(root, p, q)
    #     depth, node = self.lca
    #     return node

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> 'TreeNode':
        if root:
            left = self.lowestCommonAncestor(root.left, p, q)
            right = self.lowestCommonAncestor(root.right, p, q)

            if (left and right) or (root in [p, q]):
                return root
            else:
                return left or right


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
node = Solution().lowestCommonAncestor(root, root.left, root.left.right.right)

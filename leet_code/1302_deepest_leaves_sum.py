"""
1302. Deepest Leaves Sum
https://leetcode.com/problems/deepest-leaves-sum/

Given a binary tree, return the sum of values of its deepest leaves.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode):
        val, depth = self.DFS(root)
        return val


    def DFS(self, root, depth=0):
        if root:
            if root.left == None and root.right == None:
                if depth == 0:
                    return root.val

                return root.val, depth
            else:
                # val, depth
                left = self.DFS(root.left, depth+1)
                right = self.DFS(root.right, depth+1)

                if left[1] == right[1]:
                    return left[0] + right[0], left[1]
                else:
                    deepest = max(left, right, key=lambda x: x[1])
                    return deepest
        else:
            return 0, 0


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(7)
root.right.right = TreeNode(6)
root.right.right.right = TreeNode(8)
assert Solution().deepestLeavesSum(root = root) == 15

root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
assert Solution().deepestLeavesSum(root = root) == 19

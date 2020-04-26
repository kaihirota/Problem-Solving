"""
101. Symmetric Tree

https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reflect(self, root: TreeNode):
        if root:
            left = self.reflect(root.left)
            right = self.reflect(root.right)
            root.left = right
            root.right = left

            return root


    def DFS(self, left: TreeNode, right: TreeNode):
        if left and right:
            if left.val == right.val:
                left_result = self.DFS(left.left, right.left)
                right_result = self.DFS(left.right, right.right)

                if left_result == True and right_result == True:
                    return True
                else:
                    return False
            else:
                return False
        elif (left and not right) or (right and not left):
            return False
        elif not left and not right:
            return True


    def isSymmetric(self, root: TreeNode) -> bool:
        if root:
            if root.left == None and root.right == None:
                return True
            elif (root.left and not root.right) or (root.right and not root.left):
                return False
            elif root.right:
                root.right = self.reflect(root.right)
                result = self.DFS(root.left, root.right)
                return result

#solution
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False



node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.left = None
node.left.right = TreeNode(3)
node.right.left = TreeNode(3)
node.right.right = None
print(Solution().isSymmetric(node) == True)

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.left = None
node.left.right = TreeNode(3)
node.right.left = None
node.right.right = TreeNode(3)
print(Solution().isSymmetric(node) == False)

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(3)
node.right.left = TreeNode(3)
node.right.right = TreeNode(4)
print(Solution().isSymmetric(node) == True)

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(2)
node.left.left = TreeNode(4)
node.left.right = TreeNode(3)
node.right.left = TreeNode(4)
node.right.right = TreeNode(3)
print(Solution().isSymmetric(node) == False)

node = TreeNode(1)
node.right = TreeNode(0)
node.left = TreeNode(1)
print(Solution().isSymmetric(node) == False)

node = TreeNode(1)
node.right = TreeNode(0)
node.left = TreeNode(0)
print(Solution().isSymmetric(node) == True)

node = TreeNode(1)
node.right = TreeNode(0)
print(Solution().isSymmetric(node) == False)

node = TreeNode(1)
print(Solution().isSymmetric(node) == True)

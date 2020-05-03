"""
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST:
    def __init__(self, nums: List[int]):
        self.root = TreeNode(nums[0])

        for i in range(1, len(nums)):
            self.insert_node(self.root, TreeNode(nums[i]))

    @staticmethod
    def insert_node(root: TreeNode, node: TreeNode):
        if root.left and root.right:
            if root.val > node.val:
                BST.insert_node(root.left, node)
            else:
                BST.insert_node(root.right, node)
        else:
            if root.val > node.val:
                if root.left:
                    BST.insert_node(root.left, node)
                else:
                    root.left = node
            else:
                if root.right:
                    BST.insert_node(root.right, node)
                else:
                    root.right = node

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        tree = BST(nums)
        return tree


# nums = [-10,-3,0,5,9]
nums = [0,5,9,-10,-3]
tree = Solution().sortedArrayToBST(nums)



# AVL tree implementation in Python

import sys

class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):

    def insertNode(self, root, key):

        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insertNode(root.left, key)
        else:
            root.right = self.insertNode(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),
                        self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def delete(self, root, key):

        if not root:
            return root

        elif key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right,
                                    temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)


        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def printHelper(self, currPtr, indent, last):
           if currPtr != None:
            sys.stdout.write(indent)
            if last:
                  sys.stdout.write("R----")
                  indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print(currPtr.key)

            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


myTree = AVL_Tree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]

for num in nums:
    root = myTree.insertNode(root, num)

myTree.printHelper(root, "", True)

key = 13
root = myTree.delete(root, key)

print("After Deletion: ")
myTree.printHelper(root, "", True)

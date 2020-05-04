from binary_search_tree import TreeNode, BinarySearchTree

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def getHeight(self, node):
        print('get height')
        if not node:
            return 0

        return node.height

    def getBalance(self, node):
        if not node:
            return 0

        return self.getHeight(node.left) - self.getHeight(node.right)

    def leftRotate(self, z):
        print('L rotate')

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
        print('R rotate')

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))

        return y

    def insert_one(self, value, node=None):
        if self.empty():
            self.root = TreeNode(value)
            return

        new_node = TreeNode(value)
        if node == None:
            node = self.root

        if value < node.val:
            if node.left == None:
                node.left = new_node
            else:
                self.insert_one(value, node.left)
                return
        else:
            if node.right == None:
                node.right = new_node
            else:
                self.insert_one(value, node.right)
                return

        node.height = 1 + max(self.getHeight(node.left),
                        self.getHeight(node.right))

        balanceFactor = self.getBalance(node)

        if balanceFactor > 1:
            if value < node.left.val:
                self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                self.rightRotate(node)

        elif balanceFactor < -1:
            if value > node.right.val:
                self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                self.leftRotate(node)

        new_node.parent = node

    def remove(self, node, value):

        if not node:
            return node

        elif value < node.val:
            node.left = self.remove(node.left, value)

        elif value > node.val:
            node.right = self.remove(node.right, value)

        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.get_min(node.right)
            node.val = temp.val
            node.right = self.remove(node.right, temp.val)

        if node is None:
            return node

        node.height = 1 + max(self.getHeight(node.left),
                            self.getHeight(node.right))

        balanceFactor = self.getBalance(node)

        if balanceFactor > 1:
            if self.getBalance(node.left) >= 0:
                self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                self.rightRotate(node)
        elif balanceFactor < -1:
            if self.getBalance(node.right) <= 0:
                self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                self.leftRotate(node)

        return node


if __name__ == '__main__':
    # nums = list(range(10))
    nums = [3, 5, 1, 1, 4, 6, 8, 5, -4, -2, -8]
    # nums = [33, 13, 52, 9, 21, 61, 8, 11]
    avl = AVLTree()
    avl.insert(nums)





# """
# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
#
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
# """
# from typing import List
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         tree = BST(nums)
#         return tree
#
# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         tree = BST(nums)
#         return tree
#
# # nums = [-10,-3,0,5,9]
# nums = [0,5,9,-10,-3]
# tree = Solution().sortedArrayToBST(nums)

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

class Solution:
    def constructBST(self, nums: List[int], left=0, right=None) -> TreeNode:
        if right == None:
            right = len(nums)-1

        if left > right:
            return None

        midpoint = (left + right) // 2
        node = TreeNode(nums[midpoint])
        node.left = self.constructBST(nums=nums, left=left, right=midpoint-1)
        node.right = self.constructBST(nums=nums, left=midpoint+1, right=right)

        return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        node = self.constructBST(nums=nums)
        return node


tree = Solution().sortedArrayToBST(nums = [-10,-3,0,5,9])

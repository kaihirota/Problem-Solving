"""
654. Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree/

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        max_val = max(nums)
        max_idx = nums.index(max_val)
        root = TreeNode(max_val)

        if max_idx != 0:
            root.left = self.constructMaximumBinaryTree(nums[:max_idx])

        if max_idx != len(nums) - 1:
            root.right = self.constructMaximumBinaryTree(nums[max_idx+1:])

        return root

    def constructMaximumBinaryTree(self, nums):
        stack = []

    	for num in nums:
    		node = TreeNode(num)
    		while stack and num > stack[-1].val:
    			node.left = stack.pop()

    		if stack:
    			stack[-1].right = node
    		stack.append(node)

    	return stack[0]

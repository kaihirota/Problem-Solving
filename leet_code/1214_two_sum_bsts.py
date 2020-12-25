"""
1214. Two Sum BSTs
https://leetcode.com/problems/two-sum-bsts/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        nodes = [root1]
        seen = set()
        while nodes:
            node = nodes.pop()
            if node:
                seen.add(node.val)
                nodes.append(node.left)
                nodes.append(node.right)

        nodes = [root2]
        while nodes:
            node = nodes.pop()
            if node:
                if target - node.val in seen:
                    return True
                nodes.append(node.left)
                nodes.append(node.right)

        return False

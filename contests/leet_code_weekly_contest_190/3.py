from typing import List
from collections import defaultdict
import copy
from collections import Counter
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution:
#     def DFS(self, node, memo=None, depth=1):
#         if memo == None:
#             memo = defaultdict(int)
#
#         if node and node.val:
#             memo[node.val] += 1
#
#             if not node.left and not node.right and depth >= 3:
#                 odd_found = False
#                 for val, freq in memo.items():
#                     if freq % 2 == 1:
#                         if odd_found == False:
#                             odd_found = True
#                         else:
#                             return 0
#                 print(memo, node)
#                 return 1
#             else:
#                 return self.DFS(node.left, memo, depth+1) + self.DFS(node.right, memo, depth+1)
#
#         return 0
#
#     def pseudoPalindromicPaths (self, root: TreeNode) -> int:
#         return self.DFS(root)


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def pseudoPalindromicPaths (self, root: TreeNode) -> int:

        self.paths = 0
        self.counts = defaultdict(int)

        def dfs(node, odd_count):

            if node is None:
                return

            self.counts[node.val] += 1
            if self.counts[node.val] % 2 == 0:
                odd_count -= 1
            else:
                odd_count += 1

            if not node.left and not node.right and odd_count <= 1:
                self.paths += 1

            dfs(node.left, odd_count)
            dfs(node.right, odd_count)
            self.counts[node.val] -= 1

        dfs(root, 0)
        return self.paths


node = TreeNode(2)
node.left = TreeNode(3)
node.right = TreeNode(1)
node.left.left = TreeNode(3)
node.left.right = TreeNode(1)
node.right.right = TreeNode(1)
print(Solution().pseudoPalindromicPaths(node))

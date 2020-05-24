# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, maxnum=float('-inf')) -> int:
        if root and root.val:
            if root.val >= maxnum:
                return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val)
            else:
                return self.goodNodes(root.left, maxnum) + self.goodNodes(root.right, maxnum)
        else:
            return 0

    # # solution
    # def goodNodes(self, root: TreeNode) -> int:
    #     def dfs(root, pathBiggest):
    #         if not root:
    #             return 0
    #         if pathBiggest <= root.val:
    #             return dfs(root.left,root.val) + dfs(root.right,root.val) + 1
    #         else:
    #             return dfs(root.left,pathBiggest) + dfs(root.right,pathBiggest)
    #
    #     return dfs(root, root.val)


# node = TreeNode(3)
# node.left = TreeNode(1)
# node.right = TreeNode(4)
# node.left.left = TreeNode(3)
# node.left.right = TreeNode(None)
# node.right.left = TreeNode(1)
# node.right.right = TreeNode(5)
# assert Solution().goodNodes(node) == 4
# assert Solution().goodNodes(TreeNode(1)) == 1
#
# node = TreeNode(3)
# node.left = TreeNode(3)
# node.left.left = TreeNode(4)
# node.left.right = TreeNode(2)
# assert Solution().goodNodes(node) == 3

node = TreeNode(2)
node.left = TreeNode(-2)
node.right = TreeNode(-5)
node.left.left = TreeNode(2)
node.left.right = TreeNode(-2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(-1)
node.left.left.left = TreeNode(None)
node.left.left.right = TreeNode(0)
node.left.right.left = TreeNode(None)
node.left.right.right = TreeNode(1)
node.right.left.left = TreeNode(None)
node.right.left.right = TreeNode(None)
node.right.right.left = TreeNode(2)
node.right.right.right = TreeNode(-1)
node.left.left.left.left = TreeNode(None)
node.left.left.left.right = TreeNode(5)
node.left.left.right.left = TreeNode(None)
node.left.left.right.right = TreeNode(None)
node.left.right.left.left = TreeNode(1)
node.left.right.left.right = TreeNode(3)
node.left.right.right.left = TreeNode(None)
node.left.right.right.right = TreeNode(None)
node.right.left.left.left = TreeNode(None)
node.right.left.left.right = TreeNode(None)
node.right.left.right.left = TreeNode(None)
node.right.left.right.right = TreeNode(3)
node.right.right.left.left = TreeNode(None)
node.right.right.left.right = TreeNode(-5)
node.right.right.right.left = TreeNode(2)
node.right.right.right.right = TreeNode(-4)
node.left.left.left.right.left = TreeNode(None)
node.left.left.left.right.right = TreeNode(None)
node.left.right.left.left.left = TreeNode(None)
node.left.right.left.left.right = TreeNode(-3)
print(Solution().goodNodes(node))

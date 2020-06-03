from collections.abc import Iterable
from collections import deque
import sys
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        return f"{self.val}: ({self.left}, {self.right})"


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.values = set()

    def __str__(self):
        """
        Return a string of all the Nodes using in order traversal
        """
        return str(self.root)

    def find(self, value):
        return value in self.values

    def insert(self, *values):
        for value in values:
            if isinstance(value, Iterable):
                for item in value:
                    self.insert_one(item)
            else:
                self.insert_one(value)

    def insert_one(self, value):
        self.values.add(value)
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
            return None

        if self.BFS_insert(new_node):
            return True
        else:
            return False

    def BFS_insert(self, node: TreeNode):
        """
        attach new node to the first None found
        """
        queue = deque([self.root])
        while queue:
            curr_node = queue.popleft()
            if curr_node.left is None:
                curr_node.left = node
                return True
            else:
                queue.append(curr_node.left)

            if curr_node.right is None:
                curr_node.right = node
                return True
            else:
                queue.append(curr_node.right)
        return False

    def preorder_traverse(self, node: TreeNode):
        if node is not None:
            yield node  # Preorder Traversal
            yield from self.preorder_traverse(node.left)
            yield from self.preorder_traverse(node.right)


def maxDepth_DFS(node: TreeNode) -> int:
    """
    usage:
        maxDepth_DFS(tree.root)
    """
    if node is not None:
        return 1 + max(maxDepth_DFS(node.left), maxDepth_DFS(node.right))
    else:
        return 0

def invertTree(root: TreeNode) -> TreeNode:
    """
    Invert a binary tree.

    Example:

    Input:

         4
       /   \
      2     7
     / \   / \
    1   3 6   9
    Output:

         4
       /   \
      7     2
     / \   / \
    9   6 3   1

    usage:
        tree.root = invertTree(tree.root)
    """
    if root:
        if root.left and root.right:
            node_pointer = invertTree(root.left)
            root.left = invertTree(root.right)
            root.right = node_pointer
        elif root.left and not root.right:
            node_pointer = invertTree(root.left)
            root.left = root.right
            root.right = node_pointer
        elif root.right and not root.left:
            node_pointer = invertTree(root.right)
            root.right = root.left
            root.left = node_pointer
        return root

if __name__ == '__main__':
    nums = [3, 5, 1, 1, 4, 6, 8, 5, -4, -2, -8, 6, 8, 5, -4, -2, -8]
    tree = BinaryTree()
    tree.insert(nums)
    d = maxDepth_DFS(tree.root)
    print('depth:', d)
    print('tree:')
    print(tree)
    print('inverted tree:')
    print(invertTree(tree.root))

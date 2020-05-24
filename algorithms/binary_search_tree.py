from collections.abc import Iterable
import sys
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        # self.height = 1

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        return f"{self.val}: ({self.left}, {self.right})"


class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        """
        Return a string of all the Nodes using in order traversal
        """
        return str(self.root)

    def __reassign_nodes(self, node, new_children):
        if new_children is not None:  # reset its kids
            new_children.parent = node.parent
        if node.parent is not None:  # reset its parent
            if self.is_right(node):  # If it is the right children
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def insert(self, *values):
        for value in values:
            if isinstance(value, Iterable):
                for item in value:
                    self.insert_one(item)
            else:
                self.insert_one(value)

    def insert_one(self, value, node=None):
        if self.empty():
            self.root = TreeNode(value)
            return None

        new_node = TreeNode(value)
        if node == None:
            node = self.root

        if value < node.val:
            if node.left == None:
                new_node.parent = node
                node.left = new_node
            else:
                self.insert_one(value, node.left)
        else:
            if node.right == None:
                new_node.parent = node
                node.right = new_node
            else:
                self.insert_one(value, node.right)


    def remove(self, value):
        node = self.search(value)  # Look for the node with that label
        if node is not None:
            if node.left is None and node.right is None:  # If it has no children
                self.__reassign_nodes(node, None)
            elif node.left is None:  # Has only right children
                self.__reassign_nodes(node, node.right)
            elif node.right is None:  # Has only left children
                self.__reassign_nodes(node, node.left)
            else:
                tmp_node = self.get_max(
                    node.left
                )  # Gets the max value of the left branch
                self.remove(tmp_node.val)
                node.val = (
                    tmp_node.val
                )  # Assigns the value to the node to delete and keep tree structure

    def search(self, value):
        if self.empty():
            raise IndexError("Warning: Tree is empty! please use another.")
        else:
            node = self.root
            # use lazy evaluation here to avoid NoneType Attribute error
            while node is not None and node.val is not value:
                node = node.left if value < node.val else node.right
            return node

    def is_right(self, node):
        return node == node.parent.right

    def empty(self):
        return self.root is None

    def get_max(self, node=None):
        """
        We go deep on the right branch
        """
        if node is None:
            node = self.root
        if node is None or node.right is None:
            return node
        else:
            return self.get_max(node.right)

    def get_min(self, node=None):
        """
        We go deep on the left branch
        """
        if node is None:
            node = self.root
        if node is None or node.left is None:
            return node
        else:
            return self.get_max(node.left)

    def preorder_traverse(self, node):
        if node is not None:
            yield node  # Preorder Traversal
            yield from self.preorder_traverse(node.left)
            yield from self.preorder_traverse(node.right)


if __name__ == '__main__':
    nums = [3, 5, 1, 1, 4, 6, 8, 5, -4, -2, -8]
    # nums = [33, 13, 52, 9, 21, 61, 8, 11]
    tree = BinarySearchTree()
    tree.insert(nums)

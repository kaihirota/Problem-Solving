from binary_search_tree import TreeNode, BinarySearchTree
from collections.abc import Iterable

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def getHeight(self, node=None):
        if not node:
            return 0

        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))

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

        return y

    def rightRotate(self, z):
        print('R rotate')

        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        return y

    def update(self):
        nodes = [self.root]

        while nodes:
            node = nodes.pop()
            node = self.maintain_balance(node)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

    def maintain_balance(self, node):
        balanceFactor = self.getBalance(node)
        if balanceFactor > 1:
            if node.left and self.getBalance(node.left) < -1:
                node.left = self.leftRotate(node.left)
            node = self.rightRotate(node)
        elif balanceFactor < -1:
            if node.right and self.getBalance(node.right) < -1:
                node.right = self.leftRotate(node.right)
            node = self.leftRotate(node)
        return node

    def insert_one(self, value, node=None):
        if self.empty():
            self.root = TreeNode(value)
            return

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

        self.update()

    def remove(self, node, value):
        if not node:
            return None
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
            else:
                # if neither children are None, float up the smallest value on right side to current node, and resume recursion
                temp = self.get_min(node.right)
                node.val = temp.val
                node.right = self.remove(node.right, temp.val)

        if node is None:
            return node

        self.update()

        return node


if __name__ == '__main__':
    print('work in progress')
    # nums = list(range(10))
    # # nums = [3, 5, 1, 1, 4, 6, 8, 5, -4, -2, -8]
    # # nums = [33, 13, 52, 9, 21, 61, 8, 11]
    # avl = AVLTree()
    # avl.insert(nums)

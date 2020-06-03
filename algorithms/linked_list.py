from collections.abc import Iterable
import numpy as np
from typing import List

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        vals = self.get_values()
        vals = list(map(str, vals))
        return ", ".join(vals)

    def __iter__(self):
        """
        a = iter(ll)
        for i in range(5):
            print(next(a).value)

        for i in ll:
            print(i)
        """
        current_node = self.head

        while current_node:
            yield current_node
            current_node = current_node.next

    def get_values(self) -> List:
        vals = []
        current_node = self.head

        while current_node:
            vals.append(current_node.value)
            current_node = current_node.next

        return vals

    def insert(self, *values):
        if type(values) == np.ndarray:
            values = values.tolist()

        for value in values:
            if isinstance(value, Iterable):
                for item in value:
                    self.insert_one(item)
            else:
                self.insert_one(value)

    def insert_one(self, value):
        newnode = Node(value=value)

        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def search(self, value) -> bool:
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True
            else:
                current_node = current_node.next

        return False

    def remove(self, value):
        current_node = self.head

        while current_node:
            if current_node.value == value:
                if current_node.next is None:
                    prev_node.next = None
                else:
                    prev_node.next = current_node.next
                return True

            prev_node = current_node
            current_node = current_node.next

        return False

    def reverse(self):
        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node


if __name__ == "__main__":
    ll = LinkedList()
    n = 20
    ll.insert(np.random.randint(0, 100, size=n))
    print(ll)
    ll.reverse()
    print('reversed', ll)

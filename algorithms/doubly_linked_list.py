from collections.abc import Iterable
from linked_list import LinkedList
import numpy as np
from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)

class DoublyLinkedList(LinkedList):
    def __init__(self):
        # self.head = None
        super().__init__()
        self.tail = None

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
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def insertBefore(self, node, nodeToInsert):
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        current_node = self.head
        for i in range(position):
            current_node = current_node.next

        self.insertBefore(current_node, nodeToInsert)

    def remove(self, value):
        current_node = self.head

        while current_node:
            if current_node.value == value:
                if current_node is self.head:
                    self.head.next.prev = None
                    self.head = self.head.next
                elif current_node is self.tail:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
                else:
                    self.removeNode(current_node)
                return True

            current_node = current_node.next

        return False

    def removeNode(self, node):
        if node.prev != None and node.next != None:
            node.prev.next = node.next
            node.next.prev = node.prev

    def reverse(self):
        dummy = Node(-1)
        next_node = None
        current_node = self.head
        head_ptr = self.head

        while current_node is not None:
            next_node = current_node.next
            if dummy.next:
                dummy.next.prev = current_node
            current_node.next = dummy.next
            dummy.next = current_node
            current_node = next_node

        self.head = dummy.next
        self.tail = head_ptr

if __name__ == "__main__":
    ll = DoublyLinkedList()
    n = 20
    ll.insert(np.random.randint(0, 100, size=n))
    print(ll)
    ll.reverse()
    print('reversed', ll)

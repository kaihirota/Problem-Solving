"""
https://leetcode.com/problems/reverse-linked-list/

206. Reverse Linked List

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
import random

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

    def get_values(self):
        vals = []
        current_node = self.head

        while current_node:
            vals.append(current_node.value)
            current_node = current_node.next

        return vals

    def insert(self, value):
        newnode = Node(value=value)

        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def search(self, value):
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True
            else:
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



def test(n=20):
    ll = LinkedList()
    for i in range(n):
        ll.insert(random.randint(0, 100))

    return ll

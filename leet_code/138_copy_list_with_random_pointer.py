"""
138. Copy List with Random Pointer
https://leetcode.com/problems/copy-list-with-random-pointer/
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        original = {}
        idx = 1
        node = head
        while node:
            original[node] = idx
            idx += 1
            node = node.next

        new_list = {}
        idx = 1
        new_head = Node(0)
        curr = new_head
        node = head
        while node:
            newnode = Node(node.val)
            curr.next = newnode
            new_list[idx] = newnode
            curr = curr.next
            node = node.next
            idx += 1

        curr = new_head.next
        node = head
        while node:
            if node.random:
                curr.random = new_list[original[node.random]]

            curr = curr.next
            node = node.next

        return new_head.next

from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        map_new = defaultdict(lambda: Node(None, None, None))
        map_new[None] = None

        curr = head
        while curr:
            map_new[curr].val = curr.val
            map_new[curr].next = map_new[curr.next]
            map_new[curr].random = map_new[curr.random]
            curr = curr.next
        return map_new[head]

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        node.next = self.head
        self.head = node

    def setTail(self, node):
        node.prev = self.tail
        self.tail = node

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

    def removeNodesWithValue(self, value):
        current_node = self.head

        while current_node:
            if current_node.value == value:
                self.remove(current_node)

            current_node = current_node.next

    def remove(self, node):
        if node.prev != None and node.next != None:
            node.prev.next = node.next
            node.next.prev = node.prev

    def containsNodeWithValue(self, value):
        current_node = self.head

        while current_node:
            if current_node.value == value:
                return True

            current_node = current_node.next

        return False

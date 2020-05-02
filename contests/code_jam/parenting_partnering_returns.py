class Node:
    def __init__(self, start=None, end=None):
        self.prev = None
        self.next = None

        self.start = start
        self.end = end
        self.assigned = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def insert(self, start, end):
        newnode = Node(start=start, end=end)

        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def reverse(self):
        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        self.head = prev_node

    def get_values(self):
        vals = []
        current_node = self.head

        while current_node:
            vals.append([current_node.start, current_node.end])
            current_node = current_node.next

        return vals

tests = int(input())

for t in range(1, tests+1):

    n = int(input())
    activities = LinkedList()

    for i in range(n):
        activity = list(map(int, input().split()))
        activities.insert(activity[0], activity[1])

    activities.reverse()

    c = LinkedList()
    j = LinkedList()

    """
    for activity in activities
        if activity.start
    """

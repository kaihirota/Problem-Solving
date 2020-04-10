"""
155. Min Stack

https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""
class Node:
    def __init__(self, val):
        self.value = val
        self.currentMin = None

class MinStack:
    def __init__(self):
        self.values = []

    def push(self, x: int) -> None:
        node = Node(x)

        if len(self.values) == 0:
            node.currentMin = node.value
        else:
            if self.values[-1].currentMin >= node.value:
                node.currentMin = node.value
            elif self.values[-1].currentMin < node.value:
                node.currentMin = self.values[-1].currentMin

        self.values.append(node)

    def pop(self) -> None:
        if len(self.values) > 0:
            node = self.values.pop()
            return node.value

    def top(self) -> int:
        if len(self.values) > 0:
            return self.values[-1].value

    def getMin(self) -> int:
        if len(self.values) > 0:
            return self.values[-1].currentMin


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

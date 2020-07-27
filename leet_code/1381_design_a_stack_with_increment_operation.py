"""
1381. Design a Stack With Increment Operation
https://leetcode.com/problems/design-a-stack-with-increment-operation/

Design a stack which supports the following operations.

Implement the CustomStack class:
"""
class CustomStack:

    def __init__(self, maxSize: int):
        """
        Initializes the object with maxSize which is the maximum number of elements in the stack or do nothing if the stack reached the maxSize.
        """
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        """
        Adds x to the top of the stack if the stack hasn't reached the maxSize.
        """
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        """
        Pops and returns the top of stack
        -1 if the stack is empty.
        """
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack.pop()


    def increment(self, k: int, val: int) -> None:
        """
        Increments the bottom k elements of the stack by val.
        If there are less than k elements in the stack, just increment all the elements in the stack.
        """
        n = len(self.stack)
        if k > n:
            k = n
        for i in range(k):
            self.stack[i] += val


# O(1) solution
class CustomStack:
    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.inc = []

    def push(self, x):
        if len(self.inc) < self.n:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self):
        if not self.inc: return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()

    def increment(self, k, val):
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val



# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(maxSize=100)
for i in range(25):
    obj.push(i)

print(obj.stack)

for i in range(5):
    obj.pop()

print(obj.stack)

obj.increment(2, val=100)
print(obj.stack)

"""
716. Max Stack
https://leetcode.com/problems/max-stack/
"""
class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> int:
        if len(self.data) > 0:
            return self.data.pop()

    def top(self) -> int:
        if len(self.data) > 0:
            return self.data[-1]

    def peekMax(self) -> int:
        return max(self.data)

    def popMax(self) -> int:
        maxnum = self.peekMax()
        for i in range(len(self.data)-1, -1, -1):
            if self.data[i] == maxnum:
                idx = i
                break

        self.data = [self.data[i] for i in range(len(self.data)) if i != idx]
        return maxnum


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

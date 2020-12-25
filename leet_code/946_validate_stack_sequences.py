"""
946. Validate Stack Sequences
https://leetcode.com/problems/validate-stack-sequences/
"""
from collections import deque
from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        arr = []

        if len(popped) == 0:
            return True

        popped = deque(popped)
        for i in range(len(pushed)):
            arr += pushed[i],
            while arr and arr[-1] == popped[0]:
                popped.popleft()
                arr.pop()
        if len(popped) == 0:
            return True
        else:
            return False


Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1]) == True
Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2]) == False
Solution().validateStackSequences(pushed = [1,2,3], popped = [1,2,3]) == True

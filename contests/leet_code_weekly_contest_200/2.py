from typing import *
from collections import deque

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        arr = deque(arr)
        win = 0
        curr = arr.popleft()
        while True:
            if curr > arr[0]:
                win += 1
                tmp = arr.popleft()
                arr.append(tmp)
            else:
                win = 1
                arr.append(curr)
                curr = arr.popleft()
            if win == k or win > len(arr):
                return curr


Solution().getWinner(arr = [2,1,3,5,4,6,7], k = 2)
Solution().getWinner(arr = [3,2,1], k = 10)
Solution().getWinner(arr = [1,9,8,2,3,7,6,4,5], k = 7)
Solution().getWinner(arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000)

from typing import *
from collections import *

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        median = arr[((len(arr) - 1) // 2)]

        diff = []
        for i in range(len(arr)):
            diff += (arr[i], abs(arr[i] - median)),

        diff.sort(key=lambda x: (x[1], x[0]), reverse=True)

        ret = []
        for i in range(k):
            ret += diff[i][0],

        return ret


print(Solution().getStrongest(arr = [-7,22,17,3], k = 2))

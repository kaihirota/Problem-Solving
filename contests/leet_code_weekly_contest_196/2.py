from typing import *
from collections import defaultdict

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        data = defaultdict(list)
        for item in left:
            data[item] += -1,
        for item in right:
            data[item] += 1,

        t = 0
        while True:
            empty = True
            for key in data.keys():
                if len(data[key]) > 0:
                    for item in data[key]:
                        key += item
                        if 0 <= key <= n:
                            data[]

                    empty = False

            if empty:

            t += 1


Solution().getLastMoment(n = 4, left = [4,3], right = [0,1])

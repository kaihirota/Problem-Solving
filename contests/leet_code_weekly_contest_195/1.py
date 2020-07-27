from typing import *
from collections import *

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        d = {
            'N': (0, 1),
            'E': (1, 0),
            'W': (-1, 0),
            'S': (0, -1)
        }
        visited = set()
        visited.add((x, y))
        for step in path:
            x2, y2 = d[step]
            x += x2
            y += y2

            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
        return False


assert Solution().isPathCrossing(path = "NES") == False
assert Solution().isPathCrossing(path = "NESWW") == True

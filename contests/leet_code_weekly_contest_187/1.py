from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        orig = set([path[0] for path in paths])
        dest = set([path[1] for path in paths])
        ret = []

        for city in dest:
            if city not in orig:
                ret.append(city)

        if len(ret) == 1:
            return ret[0]


paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(Solution().destCity(paths))

paths = [["B","C"],["D","B"],["C","A"]]
print(Solution().destCity(paths))

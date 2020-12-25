"""
1282. Group the People Given the Group Size They Belong To
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""
from collections import defaultdict
from typing import List
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)

        for i in range(len(groupSizes)):
            groups[groupSizes[i]] += i,

        ret = []
        for groupSize, members in groups.items():
            n = groupSize
            arr = []
            while members:
                arr += members.pop(),
                n -= 1
                if n == 0:
                    ret += arr,
                    n = groupSize
                    arr = []
        print(ret)
        return ret


Solution().groupThePeople(groupSizes = [3,3,3,3,3,1,3])
Solution().groupThePeople(groupSizes = [2,1,3,3,3,2])

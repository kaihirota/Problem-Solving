from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        n = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                n += 1

        return n

assert Solution().busyStudent(startTime = [4], endTime = [4], queryTime = 4) == 1

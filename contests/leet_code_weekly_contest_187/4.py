from typing import List
from collections import deque
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        rows = [deque([item for item in row]) for row in mat]
        for i in range(len(rows)):
            for j in range(1, len(rows[0])):
                rows[i][j] = mat[i][j] - mat[i][j-1]

        while k > 1:
            print(rows)
            minimum = float('inf')
            loc = None
            for i in range(len(rows)):
                if len(rows[i]) > 1 and rows[i][0] + rows[i][1] < minimum:
                    minimum = rows[i][0] + rows[i][1]
                    loc = i

            rows[loc][1] += rows[loc][0]
            rows[loc].popleft()
            k -= 1

        return sum([row[0] for row in rows])


mat = [[1,3,11],[2,4,6]]
k = 5
print(Solution().kthSmallest(mat, k))

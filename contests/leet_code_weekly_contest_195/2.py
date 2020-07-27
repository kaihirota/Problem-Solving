from typing import *
from collections import deque

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        def DFS(queue, k):

            if len(queue) == 2:
                if sum(queue) % k == 0:
                    return True
                else:
                    print(queue)
                    return False

            elif len(queue) > 2:
                x = queue.popleft()
                n = len(queue)

                for i in range(n):
                    y = queue.popleft()

                    if (x + y) % k == 0:
                        result = DFS(queue, k)
                        print(i, result, queue)
                        if result is True:
                            return True

                    queue.append(y)

                return False

        return DFS(deque(arr), k)


# assert Solution().canArrange(arr = [1,2,3,4,5,10,6,7,8,9], k = 5) == True
# assert Solution().canArrange(arr = [1,2,3,4,5,6], k = 7) == True
# assert Solution().canArrange(arr = [1,2,3,4,5,6], k = 10) == False
# assert Solution().canArrange(arr = [-10,10], k = 2) == True
# assert Solution().canArrange(arr = [-1,1,-2,2,-3,3,-4,4], k = 3) == True

arr = [9606,4830,4037,-1054,3308,6966,6528,3953,473,-388,9878,-3797,2598,
-3283,5813,-6446,-3625,-107,-8756,-3053,-2131,6609,4192,7408,1115,7456,
-5674,1219,-8548,540,-9630,-4858,-2453,-726,9902,6192,-7996,1459,-1980,
4285,-2659,4156,-2303,-855]
k = 10
print(Solution().canArrange(arr = arr, k = k))
# assert Solution().canArrange(arr = arr, k = k) == False

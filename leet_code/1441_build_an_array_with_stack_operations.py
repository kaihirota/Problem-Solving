from typing import List
from collections import deque
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ret = []
        target2 = deque(target)
        nums = deque(list(range(1, n+1)))

        while nums and target:
            if not nums or not target2:
                break

            if nums[0] == target2[0]:
                ret.append('Push')
                _ = nums.popleft()
                _ = target2.popleft()
            else:
                ret.append('Push')
                ret.append('Pop')
                _ = nums.popleft()

        return ret


assert Solution().buildArray(target = [1,3], n = 3) == ["Push","Push","Pop","Push"]
assert Solution().buildArray(target = [1,2,3], n = 3) == ["Push","Push","Push"]

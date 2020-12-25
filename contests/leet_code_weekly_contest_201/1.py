from typing import *
from collections import *

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        for i in range(n):
            ret += nums[i],
            ret += nums[i + n],
        return ret


print(Solution().shuffle(nums = [2,5,1,3,4,7], n = 3))

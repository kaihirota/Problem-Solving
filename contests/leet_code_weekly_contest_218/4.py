from typing import *

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

assert Solution().minimumIncompatibility(nums = [1,2,1,4], k = 2) == 4
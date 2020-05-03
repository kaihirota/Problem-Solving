from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        counter = None
        for i in range(len(nums)):
            if counter == None and nums[i] == 1:
                counter = 0
            elif nums[i] == 1:
                if counter < k:
                    return False
                else:
                    counter = 0
            elif counter != None and nums[i] == 0:
                counter += 1

        return True


assert Solution().kLengthApart(nums = [1,0,0,0,1,0,0,1], k = 2) == True
assert Solution().kLengthApart(nums = [1,0,0,1,0,1], k = 2) == False
assert Solution().kLengthApart(nums = [1,1,1,1,1], k = 0) == True
assert Solution().kLengthApart(nums = [0,1,0,1], k = 1) == True

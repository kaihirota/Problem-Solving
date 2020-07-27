from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        for i in range(1, len(nums)-1):
            l, r = i - 1, i + 1
            current_len = 0
            while (l >= 0 and r < len(nums)) and (nums[l] == 1 or nums[r] == 1):
                print(l, r, longest)
                if nums[l] == 1:
                    l -= 1
                    current_len += 1
                if nums[r] == 1:
                    r += 1
                    current_len += 1

            longest = max(longest, current_len)
        print(longest)
        return longest


assert Solution().longestSubarray(nums = [1,1,0,1]) == 3
# assert Solution().longestSubarray(nums = [0,1,1,1,0,1,1,0,1]) == 5

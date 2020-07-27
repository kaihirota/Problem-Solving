from typing import List
from collections import Counter

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        ctr = Counter(nums)
        most_freq = [None, 0] # num, frequency
        prev = 0
        for num, freq in ctr.items():
            if freq > most_freq[1]:
                most_freq = [num, freq]

        if most_freq[1] == 1:
            sorted_nums = sorted(nums)
            min_diff = float('inf')
            for i in range(1, len(sorted_nums)):
                if min_diff > sorted_nums[i] - sorted_nums[i-1]:
                    min_diff = sorted_nums[i] - sorted_nums[i-1]
                    most_freq = [sorted_nums[i], 1]

        modify = []
        for i in range(len(nums)):
            modify += (i, abs(nums[i] - most_freq[0])), # idx, abs_diff

        modify = sorted(modify, key=lambda x: x[1], reverse=True)
        print(most_freq)
        print(modify)

        for i in range(3):
            idx, _ = modify[i]
            nums[idx] = most_freq[0]

        return max(nums) - min(nums)


# assert Solution().minDifference(nums = [5,3,2,4]) == 0
# assert Solution().minDifference(nums = [1,5,6,14,15]) == 1
# assert Solution().minDifference(nums = [20,66,68,57,45,18,42,34,37,58])) == 31
print(Solution().minDifference(nums = [53,60,100,85,16,68,64,31,37,78]))

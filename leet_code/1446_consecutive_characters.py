from typing import List

class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 0:
            return 0

        c = s[0]
        max_power = 0
        power = 1
        for i in range(1, len(s)):
            if s[i] == c:
                power += 1
            else:
                max_power = max(max_power, power)
                power = 1
                c = s[i]

        return max(max_power, power)


assert Solution().maxPower(s = "leetcode") == 2
assert Solution().maxPower(s = "abbcccddddeeeeedcba") == 5
assert Solution().maxPower(s = "triplepillooooow") == 5
assert Solution().maxPower(s = "hooraaaaaaaaaaay") == 11
assert Solution().maxPower(s = "tourist") == 1

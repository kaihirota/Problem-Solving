from typing import *

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ''
        for i in range(1, n+1):
            s += bin(i)[2:]
        print(s)
        ret = int(s, 2)
        print(ret)
        return ret % ((10 ** 9) + 7)

assert Solution().concatenatedBinary(1) == 1
assert Solution().concatenatedBinary(3) == 27
assert Solution().concatenatedBinary(12) == 505379714
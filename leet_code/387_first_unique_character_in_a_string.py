"""
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1

        explored = set()
        uniq = OrderedDict()

        for i, c in enumerate(s):
            if c not in explored:
                explored.add(c)
                uniq[c] = i
            elif c in explored and c in uniq:
                uniq.pop(c)

        if uniq:
            value = next(iter(uniq.values()))
            return value
        else:
            return -1


    # solution
    def firstUniqChar(self, s: str) -> int:
        letters='abcdefghijklmnopqrstuvwxyz'
        index=[s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1


assert Solution().firstUniqChar(s = "leetcode") == 0
assert Solution().firstUniqChar(s = "loveleetcode") == 2
assert Solution().firstUniqChar(s = "cc") == -1

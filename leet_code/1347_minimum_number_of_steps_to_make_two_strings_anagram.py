"""
1347. Minimum Number of Steps to Make Two Strings Anagram
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Constraints:
1 <= s.length <= 50000
s.length == t.length
s and t contain lower-case English letters only.
"""
from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return sum((Counter(s) - Counter(t)).values())

assert Solution().minSteps(s = "bab", t = "aba") == 1
assert Solution().minSteps(s = "leetcode", t = "practice") == 5
assert Solution().minSteps(s = "anagram", t = "mangaar") == 0
assert Solution().minSteps(s = "xxyyzz", t = "xxyyzz") == 0
assert Solution().minSteps(s = "friend", t = "family") == 4

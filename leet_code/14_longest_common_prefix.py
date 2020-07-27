"""
https://leetcode.com/problems/longest-common-prefix/
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        min_len = float('inf')
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
                min_word = s

        for i in range(min_len):
            for s in strs:
                if min_word[i] != s[i]:
                    return min_word[:i]
        return min_word

assert Solution().longestCommonPrefix(["flower","flow","flight"]) == 'fl'
assert Solution().longestCommonPrefix(["dog","racecar","car"]) == ''

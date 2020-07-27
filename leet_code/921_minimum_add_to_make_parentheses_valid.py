"""
921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Note:
S.length <= 1000
S only consists of '(' and ')' characters.

"""
from collections import deque

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if len(S) <= 1:
            return len(S)

        s = list(S)
        parentheses = deque(s[0])

        for i in range(1, len(s)):
            if len(parentheses) == 0:
                parentheses.append(s[i])
            elif parentheses[-1] == '(' and s[i] == ')':
                parentheses.pop()
            else:
                parentheses.append(s[i])

        return len(parentheses)


assert Solution().minAddToMakeValid("())") == 1
assert Solution().minAddToMakeValid("(((") == 3
assert Solution().minAddToMakeValid("()") == 0
assert Solution().minAddToMakeValid("()))((") == 4
assert Solution().minAddToMakeValid("(()())((") == 2

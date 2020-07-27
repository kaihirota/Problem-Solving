"""
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open = 0
        s = list(s)
        for idx, char in enumerate(s):
            if char == '(':
                open += 1
            elif char == ')':
                if open == 0:
                    s[idx] = ''
                else:
                    open -= 1

        i = len(s) - 1
        while open > 0:
            if s[i] == '(':
                s[i] = ''
                open -= 1
            i -= 1
        s = "".join(s)

        return s

Solution().minRemoveToMakeValid("lee(t(c)o)de)")
Solution().minRemoveToMakeValid("a)b(c)d")
Solution().minRemoveToMakeValid("))((")
Solution().minRemoveToMakeValid("(a(b(c)d)")

"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
"""
class Solution:
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left-1, right)
            if right > left:
                generate(p + ')', left, right-1)
            if not right:
                parens += p,
            return parens

        return generate('', n, n)

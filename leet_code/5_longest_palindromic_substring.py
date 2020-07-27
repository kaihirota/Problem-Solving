"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution:
    # Solution
    """
    approach:
        1. iterate over string
        2. at each i, expand outwards in both directions to find the largest palindromic substring
    """
    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            odd  = palindromeAt(s, i, i)
            even = palindromeAt(s, i, i+1)
            res = max(res, odd, even, key=len)
        return res

    # starting at l,r expand outwards to find the biggest palindrome
    def palindromeAt( s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

Solution().longestPalindrome("babad")

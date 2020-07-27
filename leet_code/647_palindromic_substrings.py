"""
647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.
"""
class Solution:
    # def countSubstrings(self, s: str) -> int:
    #     substr = 0
    #
    #     def is_palindrome(s):
    #         return s == s[::-1]
    #
    #     for i in range(len(s)):
    #         for j in range(i+1, len(s)+1):
    #             if is_palindrome(s[i:j]):
    #                 substr += 1
    #
    #     return substr

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and (((j-i+1) < 3) or dp[i+1][j-1])
                res += dp[i][j]

        return res

assert Solution().countSubstrings(s='abc') == 3
# assert Solution().countSubstrings(s='aaa') == 6

"""
https://leetcode.com/problems/longest-palindromic-subsequence/
516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".

https://leetcode.com/problems/longest-palindromic-subsequence/discuss/216717/Python-DP-solution-w-explanation
"""
class Solution:
    def longestPalindromeSubseq(self, s):
        """
        Use DP
        """
        dp = [[0]*len(s) for i in range(len(s))]

        for k in range(len(s)):
            for i in range(len(s)-k):
                j = i + k

                if i == j:
                    dp[i][j] = 1
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][len(s)-1]


assert Solution().longestPalindromeSubseq("bbbab") == 4

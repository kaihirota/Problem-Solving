"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.



If there is no common subsequence, return 0.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""
# from collections import deque
# from typing import List

# class Solution:
#     def LCS(self, L1: List, L2: List) -> int:
#         if L1 and L2:
#             if L1[-1] == L2[-1]:
#                 L1.pop()
#                 L2.pop()
#                 return 1 + self.LCS(L1, L2)
#             else:
#                 return max(self.LCS(L1[:-1], L2), self.LCS(L1, L2[:-1]))
#         else:
#             # either or both empty strings
#             return 0
#
#
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         L1 = list(text1)
#         L2 = list(text2)
#         return self.LCS(L1, L2)


# # solution
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         m = len(text1)
#         n = len(text2)
#         memo = [[None for _ in range(n + 1)] for _ in range(m + 1)]
#         x = self.helper(text1, text2, 0, 0, memo)
#         for row in memo:
#             print("\t".join([str(item) if item else "_" for item in row]))
#         return x
#         # return self.helper(text1, text2, 0, 0, memo)
#
#     def helper(self, text1, text2, i, j, memo):
#         if not memo[i][j]:
#             if i == len(text1) or j == len(text2):
#                 # no more common subsequence
#                 memo[i][j] = 0
#             elif text1[i] == text2[j]:
#                 memo[i][j] = 1 + self.helper(text1, text2, i + 1, j + 1, memo)
#             else:
#                 memo[i][j] = max(
#                     self.helper(text1, text2, i + 1, j, memo),
#                     self.helper(text1, text2, i, j + 1, memo),
#                 )
#         return memo[i][j]


# solution 2 https://leetcode.com/problems/longest-common-subsequence/discuss/351689/JavaPython-3-Two-DP-codes-of-O(mn)-and-O(min(m-n))-spaces-w-picture-and-analysis
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    memo[i + 1][j + 1] = 1 + memo[i][j]
                else:
                    memo[i + 1][j + 1] = max(memo[i][j + 1], memo[i + 1][j])
        return memo[-1][-1]


print(Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace") == 3)
print(Solution().longestCommonSubsequence(text1 = "abcde", text2 = "ace") == 3)
print(Solution().longestCommonSubsequence(text1 = "abc", text2 = "abc") == 3)
# print(Solution().longestCommonSubsequence(text1 = "abc", text2 = "def") == 0)
# print(Solution().longestCommonSubsequence(text1 = "acdzebf", text2 = "abcdef") == 5)
# print(Solution().longestCommonSubsequence(text1 = "abcwxy", text2 = "zacbcwzx") == 5)
# print(Solution().longestCommonSubsequence(text1 = "", text2 = "zacbcwzx") == 0)
# print(Solution().longestCommonSubsequence(text1 = "aggtab", text2 = "gxtxayb") == 4)
print(Solution().longestCommonSubsequence(text1 = "hofubmnylkra", text2 = "pqhgxgdofcvmr") == 5)
# print(Solution().longestCommonSubsequence(text1 = "ylqpejqbalahwr", text2 = "yrkzavgdmdgtqpg"))

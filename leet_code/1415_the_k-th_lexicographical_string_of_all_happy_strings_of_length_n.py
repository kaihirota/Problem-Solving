"""
1415. The k-th Lexicographical String of All Happy Strings of Length n
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

A happy string is a string that:

consists only of letters of the set ['a', 'b', 'c'].
s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Constraints:
1 <= n <= 10
1 <= k <= 100
"""

from typing import List

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        base_happyStrings = ['a', 'b', 'c']
        happyStrings = []

        def BFS(s: List):
            if len(happyStrings) < k and len(s) < n:
                for char in base_happyStrings:
                    if s[-1] != char:
                        s.append(char)
                        BFS(s)
                        s.pop()
            elif len(s) == n:
                happyStrings.append("".join(s))

        for char in base_happyStrings:
            BFS([char])

        happyStrings = sorted(happyStrings)

        if len(happyStrings) < k:
            return ''
        else:
            return happyStrings[k-1]


assert Solution().getHappyString(n = 1, k = 3) == 'c'
assert Solution().getHappyString(n = 1, k = 4) == ''
assert Solution().getHappyString(n = 3, k = 9) == 'cab'

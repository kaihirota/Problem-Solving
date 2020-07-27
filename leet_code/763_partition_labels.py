"""
763. Partition Labels
https://leetcode.com/problems/partition-labels/

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
"""
from typing import List
from collections import defaultdict

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        letters = defaultdict(list)

        for idx, c in enumerate(S):
            if c in letters:
                letters[c][1] = idx
            else:
                letters[c] = [idx, idx] # (first, last)

        ret = []
        start, end = None, None
        for c in letters.keys():

            if start is None:
                start, end = letters[c]
            elif letters[c][0] > end:
                ret.append(end - start + 1)
                start, end = letters[c]
            else:
                end = max(end, letters[c][1])

        ret.append(end - start + 1)
        return ret


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))

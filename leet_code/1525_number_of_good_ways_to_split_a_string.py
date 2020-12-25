"""
1525. Number of Good Ways to Split a String
https://leetcode.com/problems/number-of-good-ways-to-split-a-string
"""
class Solution:
    def numSplits(self, s: str) -> int:
        left = [0] * len(s)
        right = [0] * len(s)
        s = list(s)

		# unique chars from [0:idx+1]
        letters_seen = set()
        n_letters = 0
        for idx in range(len(s)):
            if s[idx] not in letters_seen:
                letters_seen.add(s[idx])
                n_letters += 1

            left[idx] = n_letters

		# unique chars from [idx:]
        letters_seen = set()
        n_letters = 0
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] not in letters_seen:
                letters_seen.add(s[idx])
                n_letters += 1
            right[idx] = n_letters

        ret = 0
        for i in range(len(s)-1):
            if left[i] == right[i+1]:
                ret += 1
        return ret

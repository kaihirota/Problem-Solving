"""
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def encode(s):
            cmap = {}
            i = 0
            s_freq = []
            for c in s:
                if c not in cmap:
                    cmap[c] = i
                    i += 1
                s_freq.append(cmap[c])
            return s_freq

        return encode(s) == encode(t)

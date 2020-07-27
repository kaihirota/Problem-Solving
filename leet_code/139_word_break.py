"""
139. Word Break
https://leetcode.com/problems/word-break/
"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return False
        arr = [False] * len(s)
        for i in range(len(arr)):
            for word in wordDict:
                if (i - len(word) < 0 or arr[i-len(word)] == True) and s[i-len(word)+1:i+1] == word:
                    arr[i] = True
        return arr[-1]


assert Solution().wordBreak(s = "leetcode", wordDict = ["leet", "code"]) == True
assert Solution().wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]) == True
assert Solution().wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]) == False

"""
49. Group Anagrams

https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

approach:
1. convert to list, sort the characters in alphabetical order, and concatenate back to string
2. use as dictionary key
"""

class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def groupAnagrams(self, strs):
        anagrams = {}

        for word in strs:
            anagram = "".join(sorted(list(word)))

            if anagram in anagrams.keys():
                anagrams[anagram].append(word)
            else:
                anagrams[anagram] = [word]

        return list(anagrams.values())

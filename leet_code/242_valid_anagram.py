"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
from collections import Counter, defaultdict

class Solution:
    """Given two strings s and t , write a function to determine if t is an anagram of s."""
    # def isAnagram(self, s: str, t: str) -> bool:
    #     return Counter(s) == Counter(t)

    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            count_s[s[i]] += 1

        for i in range(len(t)):
            count_t[t[i]] += 1

        return count_s == count_t


assert Solution().isAnagram(s = "anagram", t = "nagaram") == True

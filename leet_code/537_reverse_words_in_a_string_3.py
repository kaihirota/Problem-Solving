"""
557. Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""
from typing import List
from collections import deque

class Solution:
    def reverse(self, word: List[str]) -> List[str]:
        i, j = 0, len(word)-1

        while i < j:
            word[i], word[j] = word[j], word[i]
            i, j = i + 1, j - 1

        return word

    def reverseWords(self, s: str) -> str:
        words = [list(word) for word in s.split()]

        for i in range(len(words)):
            words[i] = self.reverse(words[i])

        return " ".join(["".join(word) for word in words])


s = "Let's take LeetCode contest"
assert Solution().reverseWords(s) == "s'teL ekat edoCteeL tsetnoc"

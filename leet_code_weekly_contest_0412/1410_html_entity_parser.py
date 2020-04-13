"""
1410. HTML Entity Parser

https://leetcode.com/problems/html-entity-parser/

Given an array of string words. Return all strings in words which is substring of another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
Example 2:

Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
Example 3:

Input: words = ["blue","green","bu"]
Output: []


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
It's guaranteed that words[i] will be unique.
"""

import re
class Solution:
    # def stringMatching(self, words: List[str]) -> List[str]:
    def stringMatching(self, words):
        ret = []
        for word in words:
            for word2 in words:
                if word != word2:
                    if re.search(word, word2):
                        if word not in ret:
                            ret.append(word)

        return ret

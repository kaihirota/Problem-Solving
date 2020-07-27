"""
692. Top K Frequent Words
https://leetcode.com/problems/top-k-frequent-words/

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
"""
from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1

        freq = [(word, count) for word, count in freq.items()]
        freq = sorted(freq, key=lambda x: (-x[1], x[0]), reverse=False)
        print([word for word, count in freq[:k]])
        return [word for word, count in freq[:k]]

Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 2)
Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4)

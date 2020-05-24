from typing import List

class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(' ')
        words = sorted(words, key=lambda x: len(x))

        words[0] = words[0].title()
        if len(words) > 1:
            for i in range(1, len(words)):
                words[i] = words[i].lower()

        # print(" ".join(words))
        return " ".join(words)


assert Solution().arrangeWords("Leetcode is cool") == "Is cool leetcode"

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
            for idx, word in enumerate(sentence.split(), 1):
                if word.startswith(searchWord):
                    return idx
            return -1


assert Solution().isPrefixOfWord(sentence = "i love eating burger", searchWord = "burg") == 4
assert Solution().isPrefixOfWord(sentence = "this problem is an easy problem", searchWord = "pro") == 2

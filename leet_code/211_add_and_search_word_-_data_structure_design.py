"""
211. Add and Search Word - Data structure design
https://leetcode.com/problems/add-and-search-word-data-structure-design/
"""
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_word = False
#
#
# class Trie:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()
#
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         node = self.root
#
#         for char in word:
#             if not char in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#
#         node.is_word = True
#
#     def search_regex(self, word: str, node=None) -> bool:
#         """
#         Returns if the word is in the trie.
#         '.' matches any character
#         """
#         if node is None:
#             node = self.root
#
#         for idx, char in enumerate(word):
#             if char == '.':
#                 for next_node in node.children.values():
#                     if self.search_regex(word[idx+1:], next_node) or (idx == len(word) - 1 and next_node.is_word):
#                         return True
#                 return False
#             else:
#                 if char in node.children:
#                     node = node.children[char]
#                 else:
#                     return False
#         return node.is_word


# class WordDictionary:
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = Trie()
#
#     def addWord(self, word: str) -> None:
#         """
#         Adds a word into the data structure.
#         """
#         self.trie.insert(word)
#
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         """
#         return self.trie.search_regex(word)

# solution
from collections import defaultdict
class WordDictionary:
    def __init__(self):
        self.word_dict = defaultdict(set)

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].add(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            return True
        return False

obj = WordDictionary()
words = ["bad","dad","mad"]
for word in words:
    obj.addWord(word)

assert obj.search("pad") == False
assert obj.search("bad") == True
assert obj.search(".ad") == True
assert obj.search("b..") == True

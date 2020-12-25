"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root

        for char in word:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True


trie = Trie()
for word in ["app","apple","beer","add","jam","rental"]:
    trie.insert(word)

assert trie.search("apps") == False
assert trie.search("app") == True
assert trie.search("ad") == False
assert trie.search("applepie") == False
assert trie.search("rest") == False
assert trie.search("jan") == False
assert trie.search("rent") == False
assert trie.search("beer") == True
assert trie.search("jam") == True

assert trie.startsWith("apps") == False
assert trie.startsWith("app") == True
assert trie.startsWith("ad") == True
assert trie.startsWith("applepie") == False
assert trie.startsWith("rest") == False
assert trie.startsWith("jan") == False
assert trie.startsWith("rent") == True
assert trie.startsWith("beer") == True
assert trie.startsWith("jam") == True

import sys
sys.setrecursionlimit(1000000)

class TrieNode:
    def __init__(self, depth):
        self.children = [None]*26
        self.count = 0
        self.depth = depth

# Trie functions. Source: https://www.geeksforgeeks.org/trie-insert-and-search/
def _charToIndex(ch):
    return ord(ch)-ord('A')

def insert(root,key):
    pCrawl = root
    length = len(key)
    for level in range(length):
        index = _charToIndex(key[level])
        if not pCrawl.children[index]:
            pCrawl.children[index] = TrieNode(level + 1)
        pCrawl = pCrawl.children[index]
    pCrawl.count += 1

T = int (input())
for t in range(1, T+1):
	n, k = [int(_) for _ in input().split()]
	root = TrieNode(0)
	res = [0]
	for i in range(n):
		word = input()
		insert(root, word)
	def trav(node):
		acc = 0
		for child in node.children:
			if child:
				acc += trav(child)
		res[0] += ((acc + node.count)//k)*node.depth
		return (acc + node.count)%k
	trav(root)
	print ("Case #{}: {}".format(t, res[0]))

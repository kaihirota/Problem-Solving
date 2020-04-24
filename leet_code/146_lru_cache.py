"""
146. LRU Cache
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(capacity = 2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1)) # returns 1
cache.put(3, 3)    # evicts key 2
print(cache.get(2)) # returns -1 (not found)
cache.put(4, 4)    # evicts key 1
print(cache.get(1)) # returns -1 (not found)
print(cache.get(3)) # returns 3
print(cache.get(4)) # returns 4

cache = LRUCache(capacity = 2)
cache.put(2, 1)
cache.put(2, 2)
print(cache.get(2))
cache.put(1, 1)
cache.put(4, 1)
print(cache.get(2))

"""
class LRUCache:
    """
    on put and get, move item to front, shift items
    on put, if capacity reached, eject least recently used
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.recency = []

    def get(self, key: int) -> int:
        if key in self.data:
            value = self.data[key]
            idx = self.recency.index(key)
            elem = self.recency.pop(idx)
            self.recency.insert(0, elem)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        if key not in self.recency:
            self.recency.insert(0, key)
        else:
            idx = self.recency.index(key)
            elem = self.recency.pop(idx)
            self.recency.insert(0, elem)

        if len(self.recency) > self.capacity:
            idx = self.recency.pop()
            del self.data[idx]


# solution
from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity):
        self.array = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.array:
            value = self.array[key]
            # Remove first
            del self.array[key]
            # Add back in
            self.array[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.array:
            # Delete existing key before refreshing it
            del self.array[key]
        elif len(self.array) >= self.capacity:
            # Delete oldest
            k, v = self.array.iteritems().next()
            del self.array[k]
        self.array[key] = value

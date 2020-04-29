from collections import Counter, defaultdict
from typing import List
class FirstUnique:

    def __init__(self, nums: List[int]):
        """ Initializes the object with the numbers in the queue """
        self.nums = nums
        self.counter = Counter(nums)
        self.uniq = []

        for num in self.counter.keys():
            if self.counter[num] == 1:
                self.uniq.append(num)


    def showFirstUnique(self) -> int:
        """ returns the value of the first unique integer of the queue, and returns -1 if there is no such integer."""
        if self.uniq:
            return self.uniq[0]
        else:
            return -1


    def add(self, value: int) -> None:
        """ insert value to the queue """
        if self.counter[value] == 1:
            self.uniq.remove(value)
        elif self.counter[value] == 0:
            self.uniq.append(value)

        self.nums.append(value)
        self.counter[value] += 1


nums = [2, 3, 5]
firstUnique = FirstUnique(nums)
assert firstUnique.showFirstUnique() == 2
firstUnique.add(5) # the queue is now [2,3,5,5]
assert firstUnique.showFirstUnique() == 2
firstUnique.add(2) # the queue is now [2,3,5,5,2]
assert firstUnique.showFirstUnique() == 3
firstUnique.add(3) # the queue is now [2,3,5,5,2,3]
assert firstUnique.showFirstUnique() == -1

nums = [7,7,7,7,7,7]
firstUnique = FirstUnique(nums)
assert firstUnique.showFirstUnique() == -1
firstUnique.add(7) # the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3) # the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3) # the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7) # the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17) # the queue is now [7,7,7,7,7,7,7,3,3,7,17]
assert firstUnique.showFirstUnique() == 17

nums = [809]
firstUnique = FirstUnique(nums)
assert firstUnique.showFirstUnique() == 809 # return 809
firstUnique.add(809) # the queue is now [809,809]
assert firstUnique.showFirstUnique() == -1

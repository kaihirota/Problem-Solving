"""
https://leetcode.com/problems/happy-number/

202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

############################################################

approach 1:
class Solution:
    def isHappy(self, n: int) -> bool:
        result = sum([int(i)**2 for i in list(str(n))])
        if result == 1:
            return True
        else:
            return self.isHappy(result)

result: RecursionError: maximum recursion depth exceeded

approach 2:
insight: noticed for non-Happy numbers, some kind of loop always start to form i.e. 2
used memoization to detect loops.
RecursionError cleared.
"""
class Solution:
    def isHappy(self, n: int, record=None) -> bool:
        if n == 1:
            return True

        result = sum([int(i)**2 for i in list(str(n))])

        if record == None:
            record = set([result])
        else:
            if result in record:
                return False
            else:
                record.add(result)

        return self.isHappy(result, record=record)

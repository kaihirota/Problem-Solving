"""
66. Plus One
https://leetcode.com/problems/plus-one/

Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carryover = 1
        idx = len(digits) - 1

        while idx >= 0:
            digits[idx] += carryover
            carryover = 0
            if digits[idx] > 9:
                carryover, digits[idx] = divmod(digits[idx], 10)
            idx -= 1
        if carryover != 0:
            return [carryover] + digits
        return digits

assert Solution().plusOne([0]) == [1]
assert Solution().plusOne([9]) == [1, 0]

"""
167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(arr, num, target):
            if len(arr) == 0:
                return False

            idx = len(arr) // 2

            if num + arr[idx] == target:
                return arr[idx]
            elif num + arr[idx] > target:
                return binary_search(arr[:idx], num, target)
            else:
                return binary_search(arr[idx+1:], num, target)


        for i in range(len(numbers)-1):
            ret = binary_search(numbers[i+1:], numbers[i], target)
            if ret is not False:
                j = numbers.index(ret)
                if i == j:
                    j += 1
                return [i+1, j+1]

    # solution
    def twoSum(self, numbers, target):
        dic = {}
        for i, num in enumerate(numbers):
            if target-num in dic:
                return [dic[target-num]+1, i+1]
            dic[num] = i

assert Solution().twoSum(numbers = [2,7,11,15], target = 9) == [1, 2]
assert Solution().twoSum(numbers = [5,25,75], target = 100) == [2, 3]
assert Solution().twoSum(numbers = [-1,0], target = -1) == [1, 2]
assert Solution().twoSum(numbers = [0,0,3,4], target = 0) == [1, 2]

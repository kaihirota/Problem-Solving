"""
https://leetcode.com/problems/majority-element/
https://leetcode.com/problems/majority-element/solution/

169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        record = {}

        if len(nums) > 0:
            majority = 0
            threshold = len(nums) // 2

            for num in nums:
                if num in record.keys():
                    record[num] += 1
                else:
                    record[num] = 1

                if record[num] > threshold:
                    majority = num

            return majority

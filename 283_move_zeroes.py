"""
https://leetcode.com/problems/move-zeroes/
https://leetcode.com/problems/move-zeroes/discuss/72012/Python-short-in-place-solution-with-comments.

283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = nums.count(0)
        nums[:] = [i for i in nums if i != 0]
        nums += [0] * count

class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZero = 0
        cur = 0
        while cur < len(nums):
            if nums[cur] != 0:
                nums[cur], nums[lastNonZero] = nums[lastNonZero], nums[cur]
                lastNonZero += 1

            cur += 1
    """
    A simple realization is if the current element is non-0, its' correct position can at best be it's current position or a position earlier. If it's the latter one, the current position will be eventually occupied by a non-0 ,or a 0, which lies at a index greater than 'cur' index. We fill the current position by 0 right away,so that unlike the previous solution, we don't need to come back here in next iteration.

    In other words, the code will maintain the following invariant:
    1. All elements before the slow pointer (lastNonZero) are non-zeroes.
    2. All elements between the current and slow pointer are zeroes.

    Therefore, when we encounter a non-zero element, we need to swap elements pointed by current and slow pointer, then advance both pointers. If it's zero element, we just advance current pointer.

    With this invariant in-place, it's easy to see that the algorithm will work.

    example:
        arr = [1, 3, 0, 4, 0, 5, 0]

        [1, 3, 0, 4, 0, 5, 0]
               ^ lastZero points here
        [1, 3, 0, 4, 0, 5, 0]
               ^  ^ swap 4 and 0
        [1, 3, 4, 0, 0, 5, 0]
                  ^ lastZero now points here
        [1, 3, 4, 0, 0, 5, 0]
                  ^     ^ swap 0 and 5
        [1, 3, 4, 5, 0, 0, 0]

    Complexity Analysis
        - Space Complexity : O(1). Only constant space is used.
        - Time Complexity: O(n). However, the total number of operations are optimal. The total operations (array writes) that code does is Number of non-0 elements.This gives us a much better best-case (when most of the elements are 0) complexity than last solution. However, the worst-case (when all elements are non-0) complexity for both the algorithms is same.
    """

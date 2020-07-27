"""
9. Palindrome Number
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x = list(map(int, list(str(x))))
        n = len(x)
        l, r = 0, n-1
        while l < r:
            if x[l] == x[r]:
                l, r = l+1, r-1
            else:
                return False
        return True

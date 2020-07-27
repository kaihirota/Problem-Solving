"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false


Constraints:

s consists only of printable ASCII characters.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [c for c in s if c.isalnum()]
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True
assert Solution().isPalindrome("race a car") == False

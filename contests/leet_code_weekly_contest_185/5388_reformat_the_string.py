"""
5388. Reformat The StringMy SubmissionsBack to Contest
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.

Example 4:
Input: s = "covid2019"
Output: "c2o0v1i9d"

Example 5:
Input: s = "ab123"
Output: "1a2b3"

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""
import re
class Solution:
    def reformat(self, s: str) -> str:
        nums = re.findall('\d', s)
        chars = list(re.sub('\d', '', s))

        if len(s) == 1:
            return s
        if abs(len(nums) - len(chars)) >= 2 or len(nums) == 0 or len(chars) == 0:
            return ''
        else:
            ret = []
            while nums and chars:
                elem = nums.pop()
                ret.append(elem)
                elem2 = chars.pop()
                ret.append(elem2)
            if nums:
                elem = nums.pop()
                if ret[-1].isdigit():
                    ret.insert(0, elem)
                else:
                    ret.append(elem)
            elif chars:
                elem2 = chars.pop()
                if ret[-1].isdigit():
                    ret.append(elem2)
                else:
                    ret.insert(0, elem2)
            return "".join(ret)

# s = "j"
# print(Solution().reformat(s))

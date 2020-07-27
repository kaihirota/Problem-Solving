"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return None

        self.keymap = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        def combine(digits: List, chars: str=''):
            if len(digits) > 0:
                digit = digits[0]
                letters = self.keymap[digit]
                for letter in letters:
                    combine(digits[1:], chars + letter)
            else:
                self.ret += chars,

        self.ret = []
        combine(list(digits))
        return self.ret

    # solution
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        prev = self.letterCombinations(digits[:-1])
        additional = mapping[digits[-1]]
        return [s + c for s in prev for c in additional]


Solution().letterCombinations(digits='23')
Solution().letterCombinations(digits='')

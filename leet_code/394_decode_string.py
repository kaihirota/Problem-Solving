"""
394. Decode String
https://leetcode.com/problems/decode-string/
"""
class Solution:
    # def decodeString(self, s: str) -> str:
    #     s = list(s)
    #     new = []
    #     open = False
    #     multiplier = 0
    #     for i in range(len(s)):
    #         if s[i].isdigit():
    #
    #             start = stop = i
    #             while s[stop].isdigit():
    #                 stop += 1
    #             multiplier = int("".join(s[start:stop]))
    #
    #             start = stop = i+1
    #             while s[stop] != ']':
    #                 stop += 1
    #             new += s[start+1:stop] * multiplier
    #
    #             for j in range(i, stop+1):
    #                 s[j] = ''
    #
    #         else:
    #             new += s[i],
    #
    #     print("".join(new))
    #     return "".join(new)
    def decodeString(self, s: str) -> str:
        s = list(s)
        while True:
            bracket_found = False
            for i in range(len(s)):
                if s[i] == '[':
                    start = end = i
                    bracket_found = True

            if bracket_found == False:
                break
            while s[end] != ']':
                end += 1
            num_left, num_right = start-1, start
            while s[num_left].isdigit():
                num_left -= 1

            s[num_left+1] = int("".join(s[num_left+1:num_right])) * "".join(s[start+1:end])
            for i in range(num_left+2, end+1):
                s[i] = ''

        return "".join(s)

assert Solution().decodeString(s = "3[a]2[bc]") == "aaabcbc"
assert Solution().decodeString(s = "3[a2[c]]") == "accaccacc"
assert Solution().decodeString(s = "2[abc]3[cd]ef") == "abcabccdcdcdef"
assert Solution().decodeString(s = "abc3[cd]xyz") == "abccdcdcdxyz"

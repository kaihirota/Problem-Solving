"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string, find the length of the longest substring without repeating characters.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        s = list(s)
        if n == 0:
            return 0

        longest = 1
        for i in range(n):
            chars = set(s[i])
            for j in range(i+1, n):
                if s[j] in chars:
                    break
                chars.add(s[j])
            longest = max(longest, len(chars))
        return longest

    # solution    
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i


        return max_length

assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
assert Solution().lengthOfLongestSubstring("bbbbbbb") == 1
assert Solution().lengthOfLongestSubstring("pwwkew") == 3

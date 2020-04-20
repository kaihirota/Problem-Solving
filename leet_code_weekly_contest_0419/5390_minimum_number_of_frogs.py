"""
5390. Minimum Number of Frogs CroakingMy SubmissionsBack to Contest
User Accepted:1323
User Tried:1972
Total Accepted:1333
Total Submissions:3128
Difficulty:Medium
Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.



Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1
Explanation: One frog yelling "croak" twice.
Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2
Explanation: The minimum number of frogs is two.
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".
Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
Example 4:

Input: croakOfFrogs = "croakcroa"
Output: -1


Constraints:

1 <= croakOfFrogs.length <= 10^5
All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.

"""
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croaking_frogs = 0
        frogs = {}

        s = list(croakOfFrogs)
        for char in s:
            if char == 'c':
                croaking_frogs += 1
                frogs[croaking_frogs] = ['c']
            elif char == 'r':
                for n in frogs.keys():
                    if frogs[n] == ['c']:
                        frogs[n].append(char)
                        break
            elif char == 'o':
                for n in frogs.keys():
                    if frogs[n] == list('cr'):
                        frogs[n].append(char)
                        break
            elif char == 'a':
                for n in frogs.keys():
                    if frogs[n] == list('cro'):
                        frogs[n].append(char)
                        break
            elif char == 'k':
                for n in frogs.keys():
                if frogs[croaking_frogs] == list('croa'):
                    del frogs[croaking_frogs]
                    frogs[croaking_frogs].append('k')
                    croaking_frogs -= 1

            else:
                return -1

        for i in sorted(frogs.keys(), reverse=True):
            if frogs[i] != list('croak'):
                croaking_frogs -= 1
        return -1

s = "crocakcroraoakk"
print(Solution().minNumberOfFrogs(s))

# andrew's solution
class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        count = 0
        curr_count = 0
        d = {}
        prev = {'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}

        for char in croakOfFrogs:

            d[char] = 1 if char not in d else d[char] + 1

            if char != 'c':
                if prev[char] not in d:
                    return -1

                d[prev[char]] -= 1
                if d[prev[char]] == 0:
                    del d[prev[char]]

            else:
                curr_count += 1

            if 'k' in d:
                del d['k']
                curr_count -= 1

            count = max(count, curr_count)

        return count if len(d) == 0 else -1

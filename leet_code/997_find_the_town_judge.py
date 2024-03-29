"""
997. Find the Town Judge
https://leetcode.com/problems/find-the-town-judge/

In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b. If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

Example 1:
Input: N = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: N = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:
Input: N = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:
Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

Note:
1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
"""
from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) > 0:
            trusted_count = defaultdict(int)
            trusting_count = defaultdict(int)
            for trustee, trusted in trust:
                trusted_count[trusted] += 1
                trusting_count[trustee] += 1

            for trusted, num in trusted_count.items():
                if num == N - 1 and trusting_count[trusted] == 0:
                    return trusted
        else:
            if N == 1:
                return N

        return -1


assert Solution().findJudge(N = 2, trust = [[1,2]]) == 2
assert Solution().findJudge(N = 3, trust = [[1,3],[2,3]]) == 3
assert Solution().findJudge(N = 1, trust = []) == 1

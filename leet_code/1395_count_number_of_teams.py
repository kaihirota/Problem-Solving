"""
1395. Count Number of Teams
https://leetcode.com/problems/count-number-of-teams/
"""
from typing import List
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        counter = 0
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)-1):
                for k in range(j+1, len(rating)):
                    if rating[i] > rating[j] > rating[k] or rating[i] < rating[j] < rating[k]:
                        counter += 1
        return counter


Solution().numTeams(rating = [2,5,3,4,1])

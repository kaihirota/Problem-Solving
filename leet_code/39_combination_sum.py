"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/
"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int):

        self.combinations = []

        def DFS(num, idx, arr: List[int]=[]):
            if num > 0:
                for i in range(idx, len(candidates)):
                    DFS(num-candidates[i], i, arr + [candidates[i]])
            elif num == 0:
                self.combinations += arr,


        DFS(target, 0)
        for combination in self.combinations:
            print(combination)


Solution().combinationSum(candidates = [2,3,6,7], target = 7)
# Solution().combinationSum(candidates = [2,3,5], target = 8)

from typing import List
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        idx = list(range(len(favoriteCompanies)))
        for i in range(len(favoriteCompanies)):
            s1 = set(favoriteCompanies[i])
            for j in range(len(favoriteCompanies)):
                if i != j:
                    s2 = set(favoriteCompanies[j])
                    if s1.intersection(s2) == s2 and j in idx:
                        idx.remove(j)

        return idx


assert Solution().peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]) == [0,1,4]

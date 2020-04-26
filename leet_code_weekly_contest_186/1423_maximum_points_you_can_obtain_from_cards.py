"""
1423. Maximum Points You Can Obtain from Cards
https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

There are several cards arranged in a row, and each card has an associated number of points The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.



Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
Example 4:

Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1.
Example 5:

Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202


Constraints:

1 <= cardPoints.length <= 10^5
1 <= cardPoints[i] <= 10^4
1 <= k <= cardPoints.length

"""
import copy
from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = copy.deepcopy(cardPoints)
        right = copy.deepcopy(cardPoints[::-1])
        for i in range(1, k):
            left[i] = left[i] + left[i-1]
            right[i] = right[i] + right[i-1]

        left2 = copy.deepcopy(left)
        right2 = copy.deepcopy(right)
        for i in range(0, k-1):
            left2[i] = left[i] + right[k-i-2]
            right2[i] = right[i] + left[k-i-2]

        # print(left2, right2)
        return max(max(left2[:k]), max(right2[:k]))


# andrew's Solution
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        i, j = k-1, len(cardPoints)-1

        count = 0
        for m in range(k):
            count += cardPoints[m]
        maxim = count

        while i >= 0:
            count -= cardPoints[i]
            count += cardPoints[j]
            maxim = max(maxim, count)
            i -= 1
            j -= 1

        return maxim


print(Solution().maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3) == 12)
print(Solution().maxScore(cardPoints = [2,2,2], k = 2) == 4)
print(Solution().maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7) == 55)
print(Solution().maxScore(cardPoints = [1,1000,1], k = 1) == 1)
print(Solution().maxScore(cardPoints = [1,79,80,1,1,1,200,1], k = 3) == 202)
print(Solution().maxScore(cardPoints = [56,27,75,44,38,78,12,43,2,57,71,30,78,38,60,81,61,7,23,85,28,41,47], k = 2) == 103)

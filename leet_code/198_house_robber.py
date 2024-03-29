"""
198. House Robber
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

"""
class Solution:
    # def rob(self, nums: List[int]) -> int:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            max_profit = 0
            for i in range(2, len(nums)):
                if i >= 3:
                    nums[i] = max(nums[i], nums[i]+nums[i-2], nums[i]+nums[i-3])
                else:
                    nums[i] = max(nums[i], nums[i]+nums[i-2])
                max_profit = max(nums[i], nums[i-1])
            return max_profit


# arr = [1,2,3,1] # 4
# arr = [2,7,9,3,1] # 12
# arr = [2,7,9,3,1] # 12
# arr = [2,1,1,2] # 4
# x = Solution().rob(arr)
# print(x)

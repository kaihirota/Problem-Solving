/*
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
*/

import java.util.*;
import java.util.Arrays;
import java.lang.Math;

class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            dp[i] = 1;
        }
        for (int i = 0; i < dp.length-1; i++) {
            for (int j = i+1; j < dp.length; j++) {
                if (nums[i] < nums[j]) {
                    dp[j] = Math.max(dp[j], dp[i] + 1);
                }
            }
        }
        int max = Arrays.stream(dp).max().getAsInt();
        return max;
    }
}

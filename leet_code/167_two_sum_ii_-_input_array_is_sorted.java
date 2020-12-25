/*
167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
*/

import java.util.*;
import java.util.Arrays;
import java.lang.Math;

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] ret = new int[2];
        int left = 0;
        int right = numbers.length - 1;

        while(true){
            if(numbers[left] + numbers[right] > target) {
                right--;
            }
            else if(numbers[left] + numbers[right] < target) {
                left++;
            }
            else {
                ret[0] = left+1;
                ret[1] = right+1;
                break;
            }
        }
        return ret;
    }
}

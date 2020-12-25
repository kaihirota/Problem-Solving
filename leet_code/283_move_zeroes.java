// 283. Move Zeroes
// https://leetcode.com/problems/move-zeroes/
import java.util.*;

class Solution {
  public void moveZeroes(int[] nums) {
    if (nums == null || nums.length == 0) return;
    int explorer = 0, anchor = -1;
    while (explorer < nums.length) {
      // Anchor is your first position on the array from LEFT where ZERO appears
      // As long as anchor is -1, we have NOT encountered a single ZERO element.
      if (nums[explorer] == 0 && anchor == -1)
        // Update ANCHOR
        anchor = explorer;

      if (nums[explorer] != 0 && anchor > -1) {
        swap(nums, explorer, anchor);
        ++anchor;
      }
      ++explorer;
    }
    // System.out.println("nums = " + Arrays.toString(nums));
  }

  public void swap(int nums[], int i, int j) {
    int temp = nums[i];
    nums[i] = nums[j];
    nums[j] = temp;
  }
}

public class Main {
  public static void main(String[] args) {
    int arr1[] = {0,1,0,3,12};
    for (int x : arr1) System.out.printf("%d ", x);
    System.out.printf("\n");
    new Solution().moveZeroes(arr1);
    for (int x : arr1) System.out.printf("%d ", x);
    System.out.printf("\n");
  }
}
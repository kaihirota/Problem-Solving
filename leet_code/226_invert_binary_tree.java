/*
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
*/

import java.util.*;
import java.util.Arrays;
import java.lang.Math;

class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root != null) {
            root.left = new Solution().invertTree(root.left);
            root.right = new Solution().invertTree(root.right);

            TreeNode tmp = root.left;
            root.left = root.right;
            root.right = tmp;
            return root;
        }
        return null;
    }
}

/*
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
*/

import java.util.*;
import java.util.Arrays;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        ListNode head = new ListNode(0);

        Solution solution = new Solution();
        solution.reverseList(head);
    }
}

class Solution {
    public ListNode reverseList(ListNode head) {

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode curr_node = dummy.next;
        ListNode prev_node = null;

        while (curr_node != null) {
            ListNode next_node = curr_node.next;
            curr_node.next = prev_node;
            prev_node = curr_node;
            curr_node = next_node;
        }
        dummy.next = prev_node;
        return dummy.next;
    }
}

public class ListNode {
    int val;
    ListNode next;
}

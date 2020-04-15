"""
234. Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # slow now at middle; reset fast and reverse slow
        fast = head
        
        # [4, 3, 2, 1] -> [1, 2, 3, 4]
        curr_node = slow
        prev_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        slow = prev_node
        
        # then iterate both linked lists one at a time
        while slow and fast:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

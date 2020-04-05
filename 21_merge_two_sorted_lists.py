"""
https://leetcode.com/problems/merge-two-sorted-lists/

21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    @staticmethod
    def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(None)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            elif l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next

        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next

        return dummy.next

def test():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l2.next.next.next = ListNode(6)    
    
    merged = Solution.mergeTwoLists(l1, l2)
    ret = []
    while merged:
        ret.append(merged.val)
        merged = merged.next
    
    return ret

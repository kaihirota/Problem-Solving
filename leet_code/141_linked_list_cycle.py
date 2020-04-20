"""
141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?

first approach:
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while fast:
            try:
                fast = fast.next.next
                slow = slow.next

                if fast.val == slow.val:
                    return True
            except:
                return False
        return False
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nums = set()
        current = head

        while current:
            if current.val and current.next:
                key = str(current.val) + str(current.next.val)

                if key in nums:
                    return True
                else:
                    nums.add(key)

            current = current.next
        return False

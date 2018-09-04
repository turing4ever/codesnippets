# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if head:
            pre = head
            cur = pre.next
            while cur:
                if cur.val == val:
                    pre.next = cur.next
                else:
                    pre = pre.next
                cur = cur.next
        return head

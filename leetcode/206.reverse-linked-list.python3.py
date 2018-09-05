# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        pre = None
        while p:
            n = p.next 
            pre, p.next, p = p, pre, n
        if not p:
            head = pre
        return head

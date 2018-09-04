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
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next

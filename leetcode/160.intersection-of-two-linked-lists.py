# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        A = set()
        while headA:
            A.add(headA)
            headA = headA.next
        while headB:
            if headB in A:
                return headB
            headB = headB.next
        return None

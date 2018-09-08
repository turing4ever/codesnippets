# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = None
        while slow:
            tmp = slow.next
            slow.next = pre
            slow, pre = tmp, slow
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True


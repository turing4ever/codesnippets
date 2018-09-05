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
        a = []
        while head:
            a.append(head.val)
            head = head.next
        if len(a) <= 1:
            return True
        else:
            for i in range(1, len(a)+1):
                if a[i-1] != a[-i]:
                    return False
            return True

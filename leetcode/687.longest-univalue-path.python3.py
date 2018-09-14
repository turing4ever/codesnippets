# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0
        def lp(node, pre):
            if node:
                left = lp(node.left, node.val)
                right = lp(node.right, node.val)
                self.longest = max(self.longest, left+right)
                if node.val == pre:
                    return 1 + max(left, right)
                else:
                    return 0
            else:
                return 0
        lp(root, None)
        return self.longest


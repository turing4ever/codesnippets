# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if not root.left and not root.right:
                return 1
            else:
                return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0
        

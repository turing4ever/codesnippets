# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def subSum(node, s):
            if node:
                s = subSum(node.right, s)
                s += node.val
                node.val = s
                s = subSum(node.left, s)
            return s
        subSum(root, 0)
        return root

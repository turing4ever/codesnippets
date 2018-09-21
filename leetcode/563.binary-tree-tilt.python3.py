# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def treeSum(root):
            if root:
                return root.val + treeSum(root.left) + treeSum(root.right)
            else:
                return 0
        if root:
            return abs(treeSum(root.left)-treeSum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)
        else:
            return 0

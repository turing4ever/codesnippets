# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diam  = 0
        def height(root):
            if root:
                left, right = height(root.left), height(root.right)
                self.diam = max(self.diam, left + right)
                return max(left, right) + 1 
            else:
                return 0
        height(root)
        return self.diam

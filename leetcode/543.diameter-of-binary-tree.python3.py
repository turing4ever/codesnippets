# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    diam  = 0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(root):
            if root:
                if root.left or root.right:
                    return max(height(root.left), height(root.right)) + 1 
                else:
                    return 0 
            else:
                return 0
        if root:
            if root.left and root.right:
                self.diam = max(self.diam, 2 + height(root.left) + height(root.right))
                return max(self.diam, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
            elif root.left or root.right:
                child = root.left or root.right
                self.diam = max(self.diam, 1 + height(child))
                return max(self.diam, self.diameterOfBinaryTree(child))
            else:
                return 0
        else:
            return 0

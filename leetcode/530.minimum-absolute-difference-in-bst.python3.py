# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def leftmax(node):
            if node:
                if node.right:
                    return leftmax(node.right)
                else:
                    return node.val
        def rightmin(node):
            if node:
                if node.left:
                    return rightmin(node.left)
                else:
                    return node.val
        def mindiff(root, diff):
            if root:
                if root.left:
                   diff = min(diff, abs(root.val - leftmax(root.left)))
                if root.right:
                    diff = min(diff, abs(root.val - rightmin(root.right)))
                diff = min(mindiff(root.left, diff), mindiff(root.right, diff))
            return diff
        diff = float('inf')
        return mindiff(root, diff) 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def leaf(node, side=None):
            if node:
                if node.left is None and node.right is None:
                    if side == 'left':
                        return node.val
                    else:
                        return 0
                else:
                    return leaf(node.left, 'left') + leaf(node.right, 'right')
            else:
                return 0
        return leaf(root)

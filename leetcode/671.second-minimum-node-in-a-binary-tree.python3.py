# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root and root.left and root.right:
            minis = [x for x in [root.left.val, root.right.val] if x != root.val]
            minis += [x for x in [self.findSecondMinimumValue(root.left), self.findSecondMinimumValue(root.right)] if x != -1]
            if minis:
                return min(minis)
            else:
                return -1
        else:
            return -1

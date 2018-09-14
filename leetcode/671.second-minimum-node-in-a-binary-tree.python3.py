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
            minis = [] 
            if root.left.val != root.val:
                minis.append(root.left.val)
            else:
                ret = self.findSecondMinimumValue(root.left)
                if ret != -1:
                    minis.append(ret)
            if root.right.val != root.val:
                minis.append(root.right.val)
            else:
                ret = self.findSecondMinimumValue(root.right)
                if ret != -1:
                    minis.append(ret)
            if minis:
                return min(minis)
            else:
                return -1
        else:
            return -1

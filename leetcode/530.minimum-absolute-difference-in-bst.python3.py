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
        def traverse(root):
            if root.left is not None:
                yield from traverse(root.left)
            yield  root.val
            if root.right is not None:
                yield from traverse(root.right)
        diff = None 
        pre  = None
        for i in traverse(root):
            # print(i, pre, diff)
            if pre is not None: 
                if diff is None:
                    diff = abs(pre - i)
                else:
                    diff = min(diff, abs(pre-i))
            pre = i
        return diff

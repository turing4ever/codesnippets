# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        last = [root] if root else [] 
        while last:
            ret.insert(0, [n.val for n in last if n])
            last = [x for n in last for x in (n.left, n.right) if x] 
        return ret

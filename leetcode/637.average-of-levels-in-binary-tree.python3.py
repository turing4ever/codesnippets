# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        level = [root] if root else []
        ret = []
        while level:
            values = [n.val for n in level]
            if values:
                ret.append(sum(values)/len(values))
            nextlevel = [child for n in level for child in (n.left, n.right) if child]
            level = nextlevel
        return ret

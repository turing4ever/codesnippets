# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cnt = Counter()
        def traverse(root, counter):
            if root:
                counter[root.val] += 1
                traverse(root.left, counter)
                traverse(root.right, counter)
        traverse(root, cnt)
        max_cnt = max(cnt.itervalues()) if cnt else 0 
        return [k for k, v in cnt.iteritems() if v == max_cnt] 

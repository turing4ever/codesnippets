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
        top = cnt.most_common()
        if top:
            top_freq = top[0][1]
            return [e[0] for e in cnt.most_common() if e[1] == top_freq]
        else:
            return  []
               

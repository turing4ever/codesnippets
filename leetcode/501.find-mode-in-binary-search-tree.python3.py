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
        def traverse(node, freq):
            if node:
                freq[node.val] += 1
                traverse(node.left, freq)
                traverse(node.right, freq)
        freq = Counter() 
        traverse(root, freq)
        top = freq.most_common()
        ret = []
        if top:
            ret = [x[0] for x in top if x[1] == top[0][1]]
        return ret
        

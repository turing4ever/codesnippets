# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def inorder(node):
            if node:
                if node.left:
                    yield from inorder(node.left)
                yield node
                if node.right:
                    yield from inorder(node.right)
        def paths(node, s):
            if node:
                e = 1 if node.val==s else 0
                return e + paths(node.left, s-node.val) + paths(node.right, s-node.val) 
            else:
                return 0
        total = 0
        for n in inorder(root):
            total += paths(n, sum)
        return total

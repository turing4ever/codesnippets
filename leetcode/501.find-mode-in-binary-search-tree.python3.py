# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        def inorder(node):
            if node:
                if node.left:
                    yield from inorder(node.left)
                yield node.val
                if node.right:
                    yield from inorder(node.right)
        
        out = []
        max_mode = 0
        mode = 0
        prev_val = None
        for v in inorder(root):
            if prev_val is None or v != prev_val:
                prev_val = v
                mode = 1
            else:
                mode += 1
            if max_mode < mode:
                max_mode = mode
        print(max_mode)
        mode = 0
        prev_val = None
        for w in inorder(root):
            if prev_val is None or w != prev_val:
                prev_val = w 
                mode = 1
            else:
                mode += 1
            print(mode)
            if mode == max_mode:
                out.append(w)

        return out

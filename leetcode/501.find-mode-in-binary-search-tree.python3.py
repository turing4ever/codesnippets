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
        max_num = 0
        cur_num = 0
        cur_v = -1
        for v in inorder(root):
            if cur_v != v:
                if cur_num == max_num:
                    out.append(cur_v)
                elif cur_num > max_num:
                    out = [cur_v]
                    max_num = cur_num
                cur_v = v
                cur_num = 0
            cur_num += 1
        else:
            if cur_num == max_num:
                out.append(cur_v)
            elif cur_num > max_num:
                out = [cur_v]
        return out

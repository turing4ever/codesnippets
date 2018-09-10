# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        while q:
            tmp = []
            for n in q:
                if n:
                    tmp.append(n.left)
                    tmp.append(n.right)
            #if tmp and len(tmp) != 2 * len(q):
            #    return False
            for i in range(len(tmp)//2):
                if not tmp[i] and not tmp[len(tmp)-1-i]:
                    continue
                elif not tmp[i] or not tmp[len(tmp)-1-i]:
                    return False
                elif tmp[i].val != tmp[len(tmp)-1-i].val:
                    return False
            q = tmp
        return True

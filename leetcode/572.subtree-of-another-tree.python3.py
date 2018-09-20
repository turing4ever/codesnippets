class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def same(r1, r2):
            if r1 and r2:
                return r1.val==r2.val and same(r1.left, r2.left) and same(r1.right, r2.right)                
            elif not r1 and not r2:
                return True
            else:
                return False
        if s and t:
            return same(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        elif not s and not t:
            return True
        else:
            return False

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        s = ''
        if t:
            s += str(t.val)
            if t.left and not t.right:
                s = s + '(' + self.tree2str(t.left) + ')'
            elif not t.left and t.right:
                s = s + '()' + '(' + self.tree2str(t.right) + ')'
            elif t.left and t.right:
                s = s + '(' + self.tree2str(t.left) + ')(' + self.tree2str(t.right) + ')'
        return s

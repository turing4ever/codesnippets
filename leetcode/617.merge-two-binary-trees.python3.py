class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        root = t1 or t2
        if root:
            merge = t1 if t1 != root else t2
            if merge:
                root.val = root.val + merge.val
                root.left = self.mergeTrees(root.left, merge.left)
                root.right = self.mergeTrees(root.right, merge.right)
        return root

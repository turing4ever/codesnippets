class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        from functools import partial
        def _find(root, v):
            if not root:
                return False
            if root.val == v:
                return True
            elif v < root.val:
                return _find(root.left, v)
            elif v > root.val:
                return _find(root.right, v)
        bst_find = partial(_find, root)
        def _traverse(root, bst, k):
            if root:
                if (root.val*2)!=k and bst_find(k-root.val):
                    return True
                if root.left and _traverse(root.left, bst, k):
                    return True
                if root.right and _traverse(root.right, bst, k):
                    return True
            return False
        return _traverse(root, root, k)

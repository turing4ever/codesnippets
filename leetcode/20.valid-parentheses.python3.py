class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = { "]": "[", "}": "{", ")": "("}
        stack = []
        for c in s:
            if c in d.values():
                stack.append(c)
            if c in d.keys():
                if not stack or d[c] != stack.pop():
                    return False
        if stack:
            return False
        else:
            return True

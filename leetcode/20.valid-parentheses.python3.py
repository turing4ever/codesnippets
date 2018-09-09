class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = []
        #'(', ')', '{', '}', '[' and ']'
        for c in s:
            if c == '(':
                brackets.append('(')
            elif c == '[':
                brackets.append('[')
            elif c == '{':
                brackets.append('{')
            elif c == ')':
                if brackets and brackets[-1] == '(':
                    brackets.pop()
                else:
                    return False
            elif c == ']':
                if brackets and brackets[-1] == '[':
                    brackets.pop()
                else:
                    return False
            elif c == '}':
                if brackets and brackets[-1] == '{':
                    brackets.pop()
                else:
                    return False
        if len(brackets) > 0:
            return False
        else:
            return True

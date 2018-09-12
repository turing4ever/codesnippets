class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        new_str = ''
        for c in str:
            if 65 <= ord(c) <= 90:
                new_str += chr(ord(c)+32)
            else:
                new_str += c
        return new_str

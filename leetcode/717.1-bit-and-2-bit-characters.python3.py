class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        last = 1 
        while i < len(bits):
            if bits[i]:
                i += 2 
                last = 2
            else:
                i += 1
                last = 1
        return last == 1

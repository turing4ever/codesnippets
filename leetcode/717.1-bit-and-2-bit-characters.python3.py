class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(bits):
            if i == len(bits) -1:
                return True
            if bits[i]:
                i += 2 
            else:
                i += 1
        return False 

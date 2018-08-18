class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ten = 0
        for i in range(len(digits)):
            pos = len(digits)-1-i
            if i==0:
                digits[pos] += 1
            if ten:
                digits[pos] += 1
                ten = 0
            if digits[pos] >= 10:
                ten = 1
                digits[pos] -= 10
        if ten:
            return [1] + digits 
        else:
            return digits

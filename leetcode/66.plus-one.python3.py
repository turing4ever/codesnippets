class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ten = 0
        for i in range(len(digits)):
            pos = len(digits)-1-i
            if pos == len(digits)-1:
                digits[pos] += 1
            if ten:
                digits[len(digits)-1-i] += 1
                ten = 0
            if digits[len(digits)-1-i] >= 10:
                ten = 1
                digits[len(digits)-1-i] -= 10
        if ten:
            return [1] + digits 
        else:
            return digits

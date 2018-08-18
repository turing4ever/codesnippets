class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        magic = lambda nums: sum(digit * 10 ** (len(nums) - 1 - i) for i, digit in enumerate(nums))
        d = magic(digits) 
        d = d + 1
        return [int(i) for i in str(d)]
        

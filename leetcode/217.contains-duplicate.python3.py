class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                return True        
        return False

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        n = sorted(nums)
        for i in range(len(n)):
            if i%2 == 0:
                total += min(n[i], n[i+1])
        return total
        

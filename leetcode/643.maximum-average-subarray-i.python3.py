class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sumk = sum(nums[:k])
        maxi = sumk
        for i in range(k, len(nums)):
            sumk = sumk + nums[i] - nums[i-k] 
            maxi = max(maxi, sumk)
        return maxi/k

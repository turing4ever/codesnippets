class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        maxi = 1
        cnt = 1 
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cnt += 1
            else:
                cnt = 1
            maxi = max(maxi, cnt)
        return maxi

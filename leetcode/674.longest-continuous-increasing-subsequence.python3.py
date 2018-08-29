class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = 0 
        cnt = 0 
        for i in range(len(nums)):
            if i-1 >= 0:
                if nums[i-1] < nums[i]:
                    cnt += 1
                else:
                    cnt = 1 
            else:
                cnt = 1
                mamxi = 1
            maxi = max(maxi, cnt)
        return maxi

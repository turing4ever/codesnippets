class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 
        max_all = nums[0]
        max_tmp = nums[0]
        for i in range(1, len(nums)):
            if max_tmp >= 0:
                max_tmp = max_tmp + nums[i]
            else:
                if nums[i] < 0:
                    pass
                elif nums[i] >=0:
                    max_tmp = nums[i]
            max_all = max(max_all, nums[i], max_tmp)
        return max_all

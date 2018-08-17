class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if len(nums) == 0:
        #    return 
        max_all = max_tmp = nums[0]
        for n in nums[1:]:
            if max_tmp >= 0:
                max_tmp = max_tmp + n
            else:
                if n < 0:
                    pass
                elif n >=0:
                    max_tmp = n
            max_all = max(max_all, n, max_tmp)
        return max_all

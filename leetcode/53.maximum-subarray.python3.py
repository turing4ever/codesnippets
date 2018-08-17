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
            max_tmp = max(n, n+max_tmp)
            max_all = max(max_all, max_tmp)
        return max_all

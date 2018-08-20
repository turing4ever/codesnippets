class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1 or k == 0:
            return
        k = k % len(nums)
        tmp = nums[-k:] + nums[:-k]
        for i in range(len(tmp)):
            nums[i] = tmp[i]

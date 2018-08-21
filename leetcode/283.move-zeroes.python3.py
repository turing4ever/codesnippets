class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nz = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nz] =  nums[i]
                nz += 1
        for i in range(nz, len(nums)):
            nums[i] = 0

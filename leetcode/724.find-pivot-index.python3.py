class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == 0:
                lsum = 0
                rsum = sum(nums[1:])
            else:
                lsum += nums[i-1]
                rsum -= nums[i]
            if lsum == rsum:
                return i
        return -1

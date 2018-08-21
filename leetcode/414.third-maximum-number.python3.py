class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max(nums)
        try:
            max2 = max([i for i in nums if i!=max1])
            max3 = max([i for i in nums if i!=max1 and i!=max2])
            return max3
        except:
            return max1

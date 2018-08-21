class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max(nums)
        try:
            max2 = max(set(nums) - {max1})
            max3 = max(set(nums) - {max1, max2})
            return max3
        except:
            return max1

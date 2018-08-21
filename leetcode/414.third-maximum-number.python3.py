class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max(nums)
        n2 = set(nums) - {max1}
        if n2:
            max2 = max(n2)
        else:
            return max1
        n3 = set(nums) - {max1, max2}
        if n3:
            max3 = max(n3)
            return max3
        else:
            return max1

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}
        if len(nums) <2 or k <1:
            return False
        for i,v in enumerate(nums):
            if v in d and i - d[v] <= k:
                return True
            d[v] = i
        return False

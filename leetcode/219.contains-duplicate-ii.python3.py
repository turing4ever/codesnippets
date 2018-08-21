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
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if i - d[nums[i]] <= k:
                    return True
                else:
                    d[nums[i]] = i
        return False

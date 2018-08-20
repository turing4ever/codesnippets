class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sort = sorted(nums)
        for i in range(1, len(sort)):
            if sort[i-1] == sort[i]:
                return True
        return False

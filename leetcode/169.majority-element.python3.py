class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
            if d[n] >= len(nums)/2:
                return n

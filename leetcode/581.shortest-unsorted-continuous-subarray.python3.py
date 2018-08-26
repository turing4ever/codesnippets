class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = sorted(nums)
        start, end = None, None 
        for i in range(len(nums)):
            if n[i] != nums[i]:
                start = i
                break
        for j in range(len(nums)-1, -1, -1):
            if n[j] != nums[j]:
                end = j
                break
        if start is None and end is None:
            return 0
        else:
            if start is None:
                return len(nums) - end + 1
            if end is None:
                return start + 1
            else:
                return end+1-start

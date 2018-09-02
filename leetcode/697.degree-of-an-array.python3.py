class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        min_len = len(nums) 
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = [i]
            else:
                freq[nums[i]].append(i)
        degree = max([len(f) for f in freq.values()]) 
        min_len = min([f[-1]+1-f[0] for f in freq.values() if len(f)==degree])
        return min_len

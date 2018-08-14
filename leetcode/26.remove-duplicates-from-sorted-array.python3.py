class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        tail = 0
        for i in range(1, len(nums)):
            if nums[i] ^ nums[tail]:
                tail = tail + 1
                nums[tail] = nums[i]
        return tail+1


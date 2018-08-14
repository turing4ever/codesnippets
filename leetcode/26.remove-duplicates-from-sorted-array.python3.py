class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[tail] == nums[i-1]:
                    nums[tail+1] = nums[i]
                tail += 1
            else:
                pass # tail doesn't move
        return tail+1


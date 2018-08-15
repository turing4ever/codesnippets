class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        head = 0 
        tail = len(nums) - 1
        while head <= tail:
            while tail >= 0 and nums[tail] == val:
                tail -= 1
            while head <= len(nums)-1 and nums[head] != val:
                head += 1       
            if head > tail:
                break
            if nums[head] == val and nums[tail] != val:
                nums[head], nums[tail] = nums[tail], nums[head]

        return head
                

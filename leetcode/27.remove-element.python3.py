class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        head, tail = 0, len(nums) - 1
        while head <= tail:
            if nums[head] == val:
                nums[head], nums[tail] = nums[tail], nums[head]
                tail -= 1
            else:
                head += 1
        return head
                

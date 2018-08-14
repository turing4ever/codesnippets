class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tmp = []
        for i in nums:
            if i != val:
                tmp.append(i)
        for j in range(len(tmp)):
            nums[j] = tmp[j]
        return len(tmp)
        

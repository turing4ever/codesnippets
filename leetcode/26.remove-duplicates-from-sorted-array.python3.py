class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct = [] 
        for n in nums:
            if n not in distinct:
                distinct.append(n)
        for i in range(len(distinct)):
            nums[i] = distinct[i]
        return len(distinct)


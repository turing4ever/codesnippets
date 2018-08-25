class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        nr = len(nums)
        nc = len(nums[0])
        if nr * nc != r * c:
            return nums
        a = []
        for row in nums:
            a += row
        ret = []
        for i in range(r):
            ret.append( a[i*c:(i+1)*c] )
        return ret
        

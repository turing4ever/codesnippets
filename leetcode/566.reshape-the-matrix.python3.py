class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) * len(nums[0]) != r * c:
            return nums
        a = sum(nums, [])
        ret = []
        for i in range(r):
            ret.append( a[i*c:(i+1)*c] )
        return ret
        

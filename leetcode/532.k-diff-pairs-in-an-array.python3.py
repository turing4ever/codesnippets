class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) < 2 or k < 0:
            return 0
        d = set() 
        ans = set() 
        for i in sorted(nums):
            if i-k in d:
                ans.add((i, i-k))
            if i+k in d:
                ans.add((i, i+k))
            d.add(i)
        return len(ans) if ans else 0

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def is_sorted(n):
            for i in range(len(n)):
                if i-1 >=0:
                    if n[i-1] > n[i]:
                        return False
            return True
        for i in range(len(nums)):
            ooo = False
            if i-1 >= 0:
                if nums[i-1] > nums[i]:
                    ooo = True
            if ooo:
                return is_sorted(nums[:i-1]+nums[i:]) or is_sorted(nums[:i]+nums[i+1:])
        return True

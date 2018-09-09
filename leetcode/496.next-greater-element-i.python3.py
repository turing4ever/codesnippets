class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        for n1 in nums1:
            found = 0
            greater = -1
            for n2 in nums2:
                 if n2 == n1:
                    found = 1
                 if found and n2 > n1:
                    greater = n2
                    break
            ret.append(greater) 
        return ret 

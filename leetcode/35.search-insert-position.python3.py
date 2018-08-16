class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        start, end = 0, len(nums)-1
        while start <= end:
            if start == end:
                if target <= nums[start]:
                    return start
                else:
                    return start + 1
            if start + 1 == end:
                if target <= nums[start]:
                    return start
                elif target > nums[start] and target < nums[end]:
                    return end
                elif target == nums[end]:
                    return end
                elif target > nums[end]:
                    return end + 1

            mid = start + (end - start)//2 
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            elif target > mid_val:
                start = mid + 1
            elif target < mid_val:
                end = mid - 1

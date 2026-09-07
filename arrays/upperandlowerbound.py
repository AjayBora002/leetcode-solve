class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
            
        lb = self.lower(nums, target)
        
        # Check if target actually exists in the array
        if lb == -1 or (lb < len(nums) and nums[lb] != target):
            return [-1, -1]
            
        ub = self.upper(nums, target)
        
        return [lb, ub - 1]
        
    def lower(self, nums, target):
        n = len(nums)
        low = 0
        lb = -1
        high = n - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lb = mid
                high = mid - 1  # FIXED: Updated relative to mid
            else:
                low = mid + 1
        return lb
        
    def upper(self, nums, target):
        n = len(nums)
        low = 0
        ub = -1
        high = n - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ub = mid
                high = mid - 1  # FIXED: Updated relative to mid
            else:
                low = mid + 1
        return ub
    





















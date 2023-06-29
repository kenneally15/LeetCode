class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0; r = len(nums)-1

        while l < r:

            m = l + (r-l)//2

            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m+1
            else:
                r = m
            
        
        if target > nums[l]:
            return l+1
        else:
            return l
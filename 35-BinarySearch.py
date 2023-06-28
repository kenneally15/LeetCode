class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0; right = len(nums)-1

        while left < right:

            mid = left + (right-left)//2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid
            
        
        if target > nums[left]:
            return left+1
        else:
            return left
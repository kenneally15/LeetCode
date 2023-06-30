class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        insertIndex = 1

        for i in range(1, len(nums)):
            
            if nums[insertIndex-1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex+=1
        
        return insertIndex